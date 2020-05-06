import tkinter as tk
from PIL import ImageTk, Image
import styles as st
from folderComponent import *
import folderComponent

class noteTemplate:
    def __init__(self, mainCanvas, relativeHeight, noteData):#created as canvas inside main canvas
        self.noteData=noteData
        self.canvas = tk.Canvas( master=mainCanvas, 
        bd = 3,
        bg = 'white',
        height = 75,
        width = 360
        )

        self.canvas.__init__(mainCanvas,
            bg = st.Theme["Primary"],
            height = 75,
            width = 360,
        )

        self.canvas.place(anchor=tk.NW, x=-1, y=relativeHeight)  #places new canvas

        self.canvas.bind("<Button-1>", lambda myFolder=self.noteData:self.click(myFolder))#this fetches a click event to each student canvas

        #self.showNoteData()


    def showNoteData(self):
        print(self.noteData)
        img = ImageTk.PhotoImage( Image.open('src/icons/folder.png').resize((40,45)))
        label=tk.Label(master=self.canvas,image=img, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0)
        label.img = img
        label.place(anchor=tk.NW,relx=0.05, rely=0.2)

        nombre = self.canvas.create_text(200, 20,text=self.noteData['name'])
    
    def click(self):
        pass