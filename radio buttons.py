from tkinter import *
root = Tk()

var = StringVar()
var.set(0)
lang_list = [("python", "python"), ("wp", "wp"), ("jQuery", "jQuery"), ("javascript", "javascript")]


def ShowChoice():
    print("You have selected choice number:", v.get())

list = Label(root, text="select your favourite programming language")
list.pack()

for txt, val in lang_list:
    r = Radiobutton(root, text=txt, variable=v, command=ShowChoice, value=val)
    r.pack()

root.mainloop()
