from tkinter import *


def aparecer():
    root = Tk()

    label_1 = Label(root, text='texto')
    entry = Entry(root)
    Button1=Button(root, text='boton')

    label_1.place(x=10, y=10)
    entry.place(x=0, y=2)
    Button1.place(x=0, y=4)

    root.mainloop()

mainRoot=Tk()

boton= Button(mainRoot, text='click', command=aparecer)
boton.place(x=0, y=0)

mainRoot.mainloop()

