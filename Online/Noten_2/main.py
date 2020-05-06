import tkinter as tk
from PIL import ImageTk, Image
import styles as st
from folderManager import *
import folderComponent
screenSize = { 'width': 360, 'height': 640 }

root = tk.Tk()
root.title('Tiendita')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)

path = 'students.json'

mgr = folderManager(path)


#If the file is not empty, then fetch de users
rawData = mgr.getAll()


folderComponent.folderComponent(root, rawData)


root.mainloop()

#How to create images
#img = ImageTk.PhotoImage( Image.open('src\img\prueba.jpg').resize((300,300)))
#canvas.create_image(10,10, image=img, anchor=tk.NW)