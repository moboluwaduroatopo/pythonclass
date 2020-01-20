from tkinter import *
# keep the question in a separate json file
q = [
    "Capital of India",
    "South most city in India",
    "South most city in India",
    "South most city in India",
]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
]

a = [1, 4,1, 4]
# x = '[{"q_name": "What is the verb to weep in the first person singular, future simple tense1?", "optiona": "I will weep","optionb":"I will have wept","optionc":"I  will be weeping","optiond":"I will have been weeping","ans":"I will weep"},{"q_name": "What is the verb to weep in the first person singular, future simple tense2?", "optiona": "I will weep","optionb":"I will have wept","optionc":"I  will be weeping","optiond":"I will have been weeping","ans":"I will weep"},{"q_name": "What is the verb to weep in the first person singular, future simple tense?", "optiona": "I will weep","optionb":"I will have wept","optionc":"I  will be weeping","optiond":"I will have been weeping","ans":"I will weep"}]'
        # self.y = json.loads(self.x)
class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        # print(b)    
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        # print(options[qn])
        for op in options[qn]:
            # print(op)
            self.opts[b_val]['text'] = op
            self.opts[b_val]['value'] =op
            b_val = b_val + 1
            # print(b_val)
    def check_q(self, qn):
        # print('here')
        # print(self.opt_selected.get())
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")
        # self.qn = self.qn - 1
        # self.display_q(self.qn)
    def next_btn(self):
        pass
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)
            print(self.display_q(self.qn))

root = Tk()
root.geometry("500x300")
app = Quiz(root)
root.mainloop()