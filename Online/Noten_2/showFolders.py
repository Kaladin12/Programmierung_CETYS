#this creates a template for every canvas shown on noStudents component
import tkinter as tk
from PIL import ImageTk, Image
import styles as st
#from folderComponent import *
from folderManager import *
import folderComponent
from showNotes import *

class folderTemplate:
    def __init__(self, mainCanvas, relativeHeight, folder):
        self.canvas = tk.Canvas() #created as canvas inside main canvas
        self.folder=folder
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
        canvas.bind("<Button-1>", lambda myFolder=self.folder:self.click(myFolder))#this fetches a click event to each student canvas
        self.showFolderData(self.folder, canvas)

    def showFolderData(self, folder, canvas):
        img = ImageTk.PhotoImage( Image.open('src/icons/folder.png').resize((40,45)))
        label=tk.Label(master=canvas,image=img, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0)
        label.img = img
        label.place(anchor=tk.NW,relx=0.05, rely=0.2)

        nombre = canvas.create_text(200, 20,text=folder['name'])
    
    def click(self, myFolder):
        newCanvas = folderComponent.initCanvasAgain() 
        path = 'students.json'
        mgr = folderManager(path)
        folderNotes = mgr.getAllNotes(self.folder["name"]) #gets every one of the chosen folder
        if folderNotes:
            height=90
            if (isinstance(folderNotes, list)):
                for i in range(len(folderNotes)):
                    noteTemplate(newCanvas, height, folderNotes[i]) #creates a new canvas inside main canvas
                    height+=75 #height of every sub-canvas
        else:
            add = ImageTk.PhotoImage(Image.open("src/icons/empty.png").resize((100,100)))
            label = tk.Button(master=canvas, image=add, bg=st.Theme["Primary"], highlightthickness = 0, bd = 0) #,command=lambda: onAddEvent(root, students))
            label.img = add  #IMPORTANT LINE, Why? I HAVE NO CLUE jajaj
            label.place(relx=0.35, rely=0.3)

            tk.Label(master=canvas, text="Empty File. Add a Folder with +", font=('Segoe UI', 14, 'normal'), bg=st.Theme["Primary"]).place(relx=0.08, rely=0.5)
            pass
