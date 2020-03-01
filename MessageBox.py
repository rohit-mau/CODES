from tkinter import *
root = Tk()
w = Message(root, text="Hello There Good Morning", width=150)
w.config(bg="lightgreen", font=("times", 20, "italic", "bold"))
w.pack()
root.mainloop()
