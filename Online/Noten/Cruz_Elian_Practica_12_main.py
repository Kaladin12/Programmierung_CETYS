import tkinter as tk
from PIL import ImageTk, Image
from Cruz_Elian_Practica_12_NoStudents import  *
import Cruz_Elian_Practica_12_styles as st
from Cruz_Elian_Practica_12_StudentManager import *
from Cruz_Elian_Practica_12_AddStudent import *
from Cruz_Elian_Practica_12_showStudents import *


screenSize = { 'width': 360, 'height': 640 }

root = tk.Tk()
root.title('Tiendita')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)

path = 'students.json'

mgr = StudentManager(path)


#If the file is not empty, then fetch de users
students = mgr.getAllStudents()

noStudentsComponent(root, students)
    #addStudentComponent(root)

root.mainloop()

#How to create images
#img = ImageTk.PhotoImage( Image.open('src\img\prueba.jpg').resize((300,300)))
#canvas.create_image(10,10, image=img, anchor=tk.NW)