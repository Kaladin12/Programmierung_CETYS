#This module should work as a template whenever there are or not students
import tkinter as tk
import Cruz_Elian_Practica_12_styles as st
from PIL import ImageTk, Image
from Cruz_Elian_Practica_12_studentDataTemplate import *
from Cruz_Elian_Practica_12_AddStudent import * 
from addFolder import *


mainRoot=None
mainCanvas = None

def showStudents(students, canvas):
    if students:
        height=90
        if(isinstance(students, list)):
            for i in range(len(students)):
                dataTemplate(canvas, height, students[i]) #creates a new canvas inside main canvas
                height+=75 #height of every sub-canvas
        else:
            dataTemplate(canvas, height, students)
    else:
        add = ImageTk.PhotoImage(Image.open("src/icons/empty.png").resize((100,100)))
        label = tk.Button(master=canvas, image=add, bg=st.Theme["Primary"], highlightthickness = 0, bd = 0, command=lambda: onAddEvent(root, students))
        label.img = add  #IMPORTANT LINE, Why? I HAVE NO CLUE jajaj
        label.place(relx=0.35, rely=0.3)

        tk.Label(master=canvas, text="Empty File. Add a Folder with +", font=('Segoe UI', 14, 'normal'), bg=st.Theme["Primary"]).place(relx=0.08, rely=0.5)
        pass

def onAddEvent(root, students):
    addFolder(root)

def initCanvasAgain():
    global mainRoot, mainCanvas
    canvas = tk.Canvas( master=mainRoot,
        bd = 3,
        bg = 'blue',
        height = 300,
        width = 300
    )

    mainCanvas.__init__(mainRoot,
        bg = st.Theme["Primary"],
        height = 300,
        width = 300
    )
    return mainCanvas


def noStudentsComponent(root, students):
    global mainRoot, mainCanvas
    mainRoot=root
    canvas = tk.Canvas( master=root,
        bd = 3,
        bg = 'blue',
        height = 300,
        width = 300
    )
    mainCanvas=canvas
    canvas.__init__(root,
        bg = st.Theme["Primary"],
        height = 300,
        width = 300,
        bd=0,
        highlightthickness = 0
    )

    canvas.place(anchor=tk.NW, relwidth=1, relheight=1)

    navbar = canvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["Accent"])

    navTitle = tk.Label(master=canvas, text="My Notes", fg=st.Theme["Text2"], bg=st.Theme["Accent"], font=('Segoe UI', 14, 'bold'))
    navTitle.place(anchor=tk.NW, x=10, y=15)
    studentsTitle = tk.Label(master=canvas, text="Folders", fg=st.Theme["Text"], bg = st.Theme["Primary"], font=('Segoe UI', 10, 'bold'))
    studentsTitle.place(anchor=tk.NW, x=8, y=60)

    add = ImageTk.PhotoImage(Image.open("src/icons/add.png").resize((30,30)))
    label = tk.Button(image=add, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0, command=lambda: onAddEvent(root, students))
    label.img = add  #IMPORTANT LINE, Why? I HAVE NO CLUE jajaj
    label.place(relx=0.85, rely=0.9)

    showStudents(students, canvas)