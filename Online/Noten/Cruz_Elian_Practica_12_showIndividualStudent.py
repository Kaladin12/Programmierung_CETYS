import tkinter as tk
from PIL import ImageTk, Image
import Cruz_Elian_Practica_12_styles as st
import Cruz_Elian_Practica_12_NoStudents as NoStudents
from Cruz_Elian_Practica_12_StudentManager import *


def goBack(root, students):
    NoStudents.noStudentsComponent(root, students)

def createWidgets(studentInfo):
    mainCanvas = NoStudents.initCanvasAgain()

    mainCanvas.place(anchor=tk.NW, relwidth=1, relheight=1)

    navbar = mainCanvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["Accent"])

    navTitle = tk.Label(master=mainCanvas, text='Notas' , fg=st.Theme["Text"], bg=st.Theme["Accent"])
    navTitle.place(anchor=tk.CENTER, x=175, y=25)

    path = 'students.json'

    mgr = StudentManager(path)
    students = mgr.getAllStudents()

    back = ImageTk.PhotoImage(Image.open("src/icons/back.png").resize((30,30)))
    label = tk.Button(image=back, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0, command=lambda: goBack(NoStudents.mainRoot, students))
    label.img = back  
    label.place(x=10, y=10)
    
    img = ImageTk.PhotoImage( Image.open('src/img/person1.jpg').resize((180,180))) #we need to add image location to json file
    label=tk.Label(master=mainCanvas,image=img, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0)
    label.img = img
    label.place(anchor=tk.NW,relx=0.24, rely=0.1)

    nombre = mainCanvas.create_text(180, 300,text='Nombre: '+studentInfo['name']+' '+studentInfo['lastPat']+' '+studentInfo['lastMat'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'bold'))

    fecha = mainCanvas.create_text(180, 350,text='Fecha Nacimiento: '+studentInfo['birth'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'bold'))

    descripcion = mainCanvas.create_text(180, 430, text='Descripción: '+studentInfo['description'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'normal'), width=280)

def main(studentInfo):
    createWidgets(studentInfo)