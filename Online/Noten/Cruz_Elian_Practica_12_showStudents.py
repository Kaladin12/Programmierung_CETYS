import tkinter as tk
from PIL import ImageTk, Image
import Cruz_Elian_Practica_12_styles as st


def showFolderData(folder, canvas):
    img = ImageTk.PhotoImage( Image.open('src/icons/folder.png').resize((40,45)))
    label=tk.Label(master=canvas,image=img, bg=st.Theme["Accent"], highlightthickness = 0, bd = 0)
    label.img = img
    label.place(anchor=tk.NW,relx=0.05, rely=0.2)

    nombre = canvas.create_text(200, 20,text=folder['name'])
