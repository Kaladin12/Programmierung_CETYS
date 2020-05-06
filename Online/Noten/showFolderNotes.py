#here every note canavs is created and showed
import tkinter as tk
from PIL import ImageTk, Image
import Cruz_Elian_Practica_12_styles as st
from Cruz_Elian_Practica_12_showStudents import *
from Cruz_Elian_Practica_12_showIndividualStudent import *
from Cruz_Elian_Practica_12_NoStudents import  *



class noteTemplate:
    def __init__(self, mainCanvas, relativeHeight, student):
        self.canvas = tk.Canvas() #created as canvas inside main canvas
        self.student=student
        self.maincanvas=mainCanvas
        canvas = tk.Canvas( master=mainCanvas, 
        bd = 3,
        bg = 'white',
        height = 75,
        width = 360
        )

        canvas.__init__(mainCanvas,
            bg = st.Theme["Primary"],
            height = 75,
            width = 360,
        )

        canvas.place(anchor=tk.NW, x=-1, y=relativeHeight)  #places new canvas
        canvas.bind("<Button-1>", lambda myStudent=student:self.click(myStudent))#this fetches a click event to each student canvas
        self.showData(self.student)

    def click(self, myStudent):
        path = 'students.json'
        mgr = StudentManager(path)

    def createWidgets(self, noteInfo):

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
        self.showData(self.student, self.canvas)

    def showData(self, noteInfo):
        img = ImageTk.PhotoImage( Image.open('src/icons/folder.png').resize((40,45)))
        label=tk.Label(master=self.maincanvas,image=img, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0)
        label.img = img
        label.place(anchor=tk.NW,relx=0.05, rely=0.2)
        print('visit')
        nombre = self.maincanvas.create_text(10, 20,text='Nombre: '+noteInfo['name'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'bold'))
        quit()
        fecha = self.maincanvas.create_text(10, 30,text='Date: '+noteInfo['date'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'bold'))

        #descripcion = canvas.create_text(10, 40, text='Descripción: '+noteInfo['description'], fill=st.Theme["Text"], font=('Segoe UI', 12, 'normal'), width=280)
