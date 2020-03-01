from tkinter import *
root = Tk()


def var_states():
    print('Read 1:%d, \nWritting 2:%d' % (var1.get(), var2.get()))
    

var1 = IntVar()
check1 = Checkbutton(root, text='Read', variable=var1)

var2 = IntVar()
check2 = Checkbutton(root, text='Writting', variable=var2)

buttton = Button(root, text='Show', command=var_states)
check1.pack(side=LEFT)
check2.pack(side=LEFT)

buttton.pack(side=LEFT)

root.mainloop()
