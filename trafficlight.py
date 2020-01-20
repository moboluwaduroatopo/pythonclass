from tkinter import *

from PIL import Image, ImageTk
# import PIL
class Trafficlight():
    def __init__(self):
        self.root=Tk()
        self.root.title('Traffic Lights')
        self.x='red'
        self.y='yellow'
        self.z='green'
        self.Frames = Frame(self.root)
        self.Frames.pack(side = BOTTOM)
        self.canvas = Canvas(self.Frames, width = 300, height = 400, bg = "black")
        self.canvas.grid(row = 0, column = 0,columnspan=2,)
        self.canvas.create_rectangle(100, 50, 200, 350)
        self.startgui()
        self.root.mainloop()
    def red(self):
        self.can1=self.canvas.create_oval(100, 50, 200, 150, fill=self.x)
        self.canvas.create_oval(100, 150, 200, 250,fill='white')
        self.canvas.create_oval(100, 250, 200, 350,fill='white')
    def yellow(self):
        self.canvas.create_oval(100, 50, 200, 150, fill='white')
        self.can2=self.canvas.create_oval(100, 150, 200, 250, fill=self.y)
        self.canvas.create_oval(100, 250, 200, 350,fill='white')
    def green(self):
        self.canvas.create_oval(100, 50, 200, 150, fill='white')
        self.canvas.create_oval(100, 150, 200, 250,fill='white')
        self.can3=self.canvas.create_oval(100, 250, 200, 350, fill=self.z)
    def startgui(self):
        self.canvas.create_oval(100, 50, 200, 150, fill='white')
        self.canvas.create_oval(100, 150, 200, 250, fill='white')
        self.canvas.create_oval(100, 250, 200, 350, fill='white')
        self.button = Button(self.Frames, text = 'Start',command=self.start) 
        self.button.grid(row = 1, column = 0,columnspan=2,)
        self.button = Button(self.Frames, text = 'Stop',command=self.stop) 
        self.button.grid(row = 1, column = 1,)
    def start(self):
        self.Frames.after(2000, self.start)
        self.Frames.after(2000, self.red) 
        self.Frames.after(3000, self.yellow) 
        self.Frames.after(3500, self.green)   
    def stop(self):
        # self.Frames.after(0000,self.stop)  
        self.canvas.itemconfig(self.can1,fill='white')
        self.canvas.itemconfig(self.can2,fill='white')
        self.canvas.itemconfig(self.can3,fill='white')
        # self.canvas.delete("all")
        # print('here')

             

Trafficlight()
 
# import tkinter as tk
# from tkinter.messagebox import _show 
  
# class Fun(tk.Tk):
#     def __init__(self):
#         tk.Frame.__init__(self)
#         self.master.title("I say things")

#         self.count = 0
#         self.count_str = tk.StringVar()
#         self.count_str.set(str(self.count))

#         tk.Entry(self.master, textvariable=self.count_str).pack()

#     def more_count(self):
#         self.after(2000, self.more_count)
#         self.count += 1
#         self.count_str.set(str(self.count))
#         self.master.after(4000, lambda : _show('Title', 'Prompting after 5 seconds')) 



# f = Fun()
# f.more_count()
# f.mainloop()