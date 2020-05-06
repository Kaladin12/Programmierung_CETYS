import tkinter as tk
import styles as st
from PIL import ImageTk, Image
from folder import *
from folderManager import *
import folderComponent as noStudents

#this module is used for the creation of folder objects inside json file

def onAddEvent(name, root):#, rootFolder, day, month, year, description, root, students):
    path = 'students.json'
    student = Folder(
        name
    ).getJSONforFolder()
    mgr = folderManager(path)
    mgr.addFolder(student)
    folders=mgr.getAll()
    #goBack(root, students)

def addFolder(root):
    canvas = noStudents.initCanvasAgain()

    canvas.place(anchor=tk.NW, relwidth=1, relheight=1)

    navbar = canvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["Accent"])

    back = ImageTk.PhotoImage(Image.open("src/icons/back.png").resize((30,30)))
    label = tk.Button(image=back, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0, command=lambda: goBack(root, []))
    label.img = back  #IMPORTANT LINE, Why? I HAVE NO CLUE
    label.place(x=10, y=10)


    navTitle = tk.Label(master=canvas, text="Add Folder", fg=st.Theme["Text2"], bg=st.Theme["Accent"], font=('Segoe UI', 14, 'bold'))
    navTitle.place(anchor=tk.NW, x=50, y=15)
    studentsTitle = tk.Label(master=canvas, text="Name", fg=st.Theme["Text"], bg = st.Theme["Primary"], font=('Segoe UI', 10, 'bold'))
    studentsTitle.place(anchor=tk.NW, x=10, y=70)

    nameInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=42)
    nameInput.place(x=11, y=110)
    nameInput.insert(0, "Name")

    addBtn = tk.Button(bg=st.Theme["Accent"], fg='white', width=38, text="ADD STUDENT",
    command=lambda: onAddEvent(
        nameInput.get(),
        root
    ))
    addBtn.place(x=11, y=550)
