import tkinter as tk
import Cruz_Elian_Practica_12_styles as st
from PIL import ImageTk, Image
from Cruz_Elian_Practica_12_Folder import *
from Cruz_Elian_Practica_12_StudentManager import *
import Cruz_Elian_Practica_12_NoStudents

def goBack(root, students):
    Cruz_Elian_Practica_12_NoStudents.noStudentsComponent(root, students)

def onAddEvent(name, ap, mat, day, month, year, description, root, students):
    path = 'students.json'
    student = Student(
        name,
        ap,
        mat,
        day+'/'+month+'/'+year,
        description
    ).getJSON()
    mgr = StudentManager(path)
    mgr.addStudent(student)
    students=mgr.getAllStudents()
    goBack(root, students)

def addStudentComponent(root, students):
    canvas = tk.Canvas( master=root,
        bd = 2,
        bg = 'blue',
        height = 300,
        width = 300
    )

    canvas.__init__(root,
        bg = st.Theme["Primary"],
        height = 300,
        width = 300
    )

    canvas.place(anchor=tk.NW, relwidth=1, relheight=1)

    navbar = canvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["Accent"])

    back = ImageTk.PhotoImage(Image.open("src/icons/back.png").resize((30,30)))
    label = tk.Button(image=back, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0, command=lambda: goBack(root, students))
    label.img = back  #IMPORTANT LINE, Why? I HAVE NO CLUE
    label.place(x=10, y=10)


    navTitle = tk.Label(master=canvas, text="Agregar", fg=st.Theme["Text2"], bg=st.Theme["Accent"], font=('Segoe UI', 14, 'bold'))
    navTitle.place(anchor=tk.NW, x=50, y=15)
    studentsTitle = tk.Label(master=canvas, text="Name", fg=st.Theme["Text"], bg = st.Theme["Primary"], font=('Segoe UI', 10, 'bold'))
    studentsTitle.place(anchor=tk.NW, x=10, y=70)

    #nameLabel = tk.Label(master=canvas, bg=st.Theme["Primary"], fg=st.Theme["Text"], text="Name:")
    #nameLabel.place(x=10, y=150)
    nameInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=42)
    nameInput.place(x=11, y=110)
    nameInput.insert(0, "Name")
    lastApInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=42, font=('Segoe UI', 10, 'normal'))
    lastApInput.place(x=11, y=150)
    lastApInput.insert(0, "First Last Name")

    lastMatInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=42)
    lastMatInput.place(x=11, y=190)
    lastMatInput.insert(0, "Second Last Name")

    birthTitle = tk.Label(master=canvas, text="Birth", fg=st.Theme["Text"], bg=st.Theme["Primary"], font=('Segoe UI', 10, 'bold'))
    birthTitle.place(anchor=tk.NW, x=10, y=230)

    dayInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=7)
    dayInput.place(x=11, y=270)
    dayInput.insert(0, "Day(01)")

    monthInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=9)
    monthInput.place(x=100, y=270)
    monthInput.insert(0, "Month(01)")

    yearInput = tk.Entry(master=canvas, bg=st.Theme["Secondary"], fg="gray", highlightthickness = 0, bd=0, width=9)
    yearInput.place(x=201, y=270)
    yearInput.insert(0, "Year(01)")

    descriptionTitle = tk.Label(master=canvas, text="Description", fg=st.Theme["Text"], bg=st.Theme["Primary"], font=('Segoe UI', 10, 'bold'))
    descriptionTitle.place(anchor=tk.NW, x=10, y=310)

    descriptionInput = tk.Text(master=canvas, height=5, width=41, highlightthickness = 0, bd=0, bg=st.Theme["Secondary"])
    descriptionInput.place(x=11, y=350)

    addBtn = tk.Button(bg=st.Theme["Accent"], fg='white', width=38, text="ADD STUDENT",
    command=lambda: onAddEvent(
        nameInput.get(),
        lastApInput.get(),
        lastMatInput.get(),
        dayInput.get(),
        monthInput.get(),
        yearInput.get(),
        descriptionInput.get("1.0", "end"),
        root, students
    ))
    addBtn.place(x=11, y=550)