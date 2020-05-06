#this creates a template for every canvas shown on noStudents component
import tkinter as tk
from PIL import ImageTk, Image
import Cruz_Elian_Practica_12_styles as st
from Cruz_Elian_Practica_12_showStudents import *
from Cruz_Elian_Practica_12_showIndividualStudent import *
from Cruz_Elian_Practica_12_NoStudents import  *
import Cruz_Elian_Practica_12_NoStudents as noStudents
from showFolderNotes import *


class dataTemplate:
    def __init__(self, mainCanvas, relativeHeight, student):
        self.canvas = tk.Canvas() #created as canvas inside main canvas
        self.student=student
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
        showFolderData(student, canvas)
    
    def click(self, myStudent):
        newCanvas = noStudents.initCanvasAgain() 
        print('click')
        height=90
        path = 'students.json'
        mgr = StudentManager(path)
        myNotes = mgr.getAllNotes(self.student["name"])
        print(myNotes)
        for note in myNotes:
            noteTemplate(newCanvas, height, note)
            height+=75



