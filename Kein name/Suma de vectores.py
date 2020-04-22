import tkinter, coordenadas, cosenos
from tkinter import ttk, messagebox
import time, numpy, matplotlib.pyplot, math
from mpl_toolkits import mplot3d
which=False
primera_vez=True
vetores=[]
class vector:
    def __init__(self, coordenadas, magnitud):
        self.coordenadas=[]
        self.lambdas=[]
        self.magnitud=0

def combo():
    global which,primera_vez
    if comboExample.get()=="Dos coordenadas":
        which=True
        a=coordenadas.coord()
        a.add()
        
    elif comboExample.get()=="Cosenos directores":
        which=False
        b=cosenos.angulos()

ventana=tkinter.Tk()
ventana.title('Suma de vectores en 3D      CRUZ ESQUIVEL ELIAN JAVIER')
ventana.minsize(100,80)
#panel 1
panel1=tkinter.PanedWindow()
panel1.grid(row=0, column=0)
label_presentacion=tkinter.Label(panel1, text="Suma de vectores en tres dimensiones")
l1=tkinter.Label(panel1,text="Cómo desea introducir sus vectores?: ")
l1.grid(row=1, column=0)
comboExample = ttk.Combobox(panel1, values=[
                                    "Dos coordenadas", 
                                    "Cosenos directores"])
comboExample.grid(row=2, column=0)
boton=ttk.Button(panel1, text="Listo", command=combo)
boton.grid(row=6, column=0)
ventana.mainloop()

#Hecho por Elian JAVIER CRUZ ESQUIVEL, ICC, CETYS UNIVERSIDAD 