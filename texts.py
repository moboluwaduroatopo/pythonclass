from tkinter import *
root =Tk()
content ="This is a test felid to write file"
mcontent=Text(root,height=30,width=60)
mcontent.grid(row=4,column=2)
# scroll=Scrollbar(root,orient="vertical",command=mcontent.yview)
# scroll.grid(row=4,column=3,sticky='ns')
# mcontent.configure(yscrollcommand = scroll.set)
mcontent.insert(END,content)
mainloop()