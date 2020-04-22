import tkinter
from tkinter import ttk, messagebox
import time, numpy, matplotlib.pyplot, math
from mpl_toolkits import mplot3d

class vector:
    def __init__(self, angulos, magnitud):
        self.angulos=[]
        self.lambdas=[]
        self.magnitud1=0
        self.magnitud2=0

primera_vez=True

class angulos:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.title('Suma de vectores en 3D      CRUZ ESQUIVEL ELIAN JAVER')
        self.ventana.minsize(640,360)
        self.which=False
        self.vetores=[]
        self.panel_cosenos_firectores=tkinter.PanedWindow(self.ventana)
        self.label_ingresa_magnitud1=tkinter.Label(self.panel_cosenos_firectores, text="Ingrese magnitud del vector: ")
        self.label_ingresa_magnitud2=tkinter.Label(self.panel_cosenos_firectores, text="Ingrese magnitud del vector: ")
        self.caja_magnitud1=tkinter.Entry(self.panel_cosenos_firectores)
        self.caja_magnitud2=tkinter.Entry(self.panel_cosenos_firectores)
        self.boton_listo1=ttk.Button(self.panel_cosenos_firectores, text='Listo', command=self.listo)
        self.label_v1=tkinter.Label(self.panel_cosenos_firectores,text="Vector 1: ")
        self.label_v2=tkinter.Label(self.panel_cosenos_firectores,text="Vector 2: ")
        self.caja_theta_x=tkinter.Entry(self.panel_cosenos_firectores)
        self.caja_theta_y=tkinter.Entry(self.panel_cosenos_firectores)
        self.caja_theta_z=tkinter.Entry(self.panel_cosenos_firectores)
        self.label_thx=tkinter.Label(self.panel_cosenos_firectores, text="θx: ")
        self.label_thy=tkinter.Label(self.panel_cosenos_firectores, text="θy: ")
        self.label_thz=tkinter.Label(self.panel_cosenos_firectores, text="θz: ")
        self.caja_theta_x2=tkinter.Entry(self.panel_cosenos_firectores)
        self.caja_theta_y2=tkinter.Entry(self.panel_cosenos_firectores)
        self.caja_theta_z2=tkinter.Entry(self.panel_cosenos_firectores)
        self.label_thx2=tkinter.Label(self.panel_cosenos_firectores, text="θx: ")
        self.label_thy2=tkinter.Label(self.panel_cosenos_firectores, text="θy: ")
        self.label_thz2=tkinter.Label(self.panel_cosenos_firectores, text="θz: ")
        self.add()
        self.ventana.mainloop()

    def add(self):
        self.panel_cosenos_firectores.grid(row=10, column=0)
        self.label_ingresa_magnitud1.grid(row=5, column=2)
        self.caja_magnitud1.grid(row=5, column=5)
        self.label_v1.grid(row=4, column=2)
        self.boton_listo1.grid(row=14, column=5)
        self.label_v2.grid(row=9, column=2)
        self.label_ingresa_magnitud1.grid(row=10, column=2)
        self.caja_magnitud2.grid(row=10, column=5)
        self.caja_theta_x2.grid(row=11, column=5)
        self.caja_theta_y2.grid(row=12, column=5)
        self.caja_theta_z2.grid(row=13, column=5) 
        self.label_thx2.grid(row=11, column=2)
        self.label_thy2.grid(row=12, column=2)
        self.label_thz2.grid(row=13, column=2) 
        self.caja_theta_x.grid(row=6, column=5)
        self.caja_theta_y.grid(row=7, column=5)
        self.caja_theta_z.grid(row=8, column=5) 
        self.label_thx.grid(row=6, column=2)
        self.label_thy.grid(row=7, column=2)
        self.label_thz.grid(row=8, column=2) 

    def listo(self):
        try:
            lista=[float(self.caja_theta_x.get()),float(self.caja_theta_y.get()),float(self.caja_theta_z.get()),float(self.caja_theta_x2.get()),float(self.caja_theta_y2.get()),float(self.caja_theta_z2.get())]
            vector1=vector(lista, float(self.caja_magnitud1.get()))
            vector1.angulos.append(lista)
            vector1.magnitud1=float(self.caja_magnitud1.get())
            vector1.magnitud2=float(self.caja_magnitud2.get())
            self.vetores.append(vector1)
        except:
            messagebox.showinfo(message="Solo introducir números", title='Error')
        self.cosenos(self.vetores[0])
            
    def cosenos(self, v1):
        #cos1=[math.cos((math.pi/180)*v1.angulos[0][0]),math.cos((math.pi/180)*v1.angulos[0][1]),math.cos((math.pi/180)*v1.angulos[0][2])]
        componentes_fuerza1=[(v1.magnitud1*math.cos((math.pi/180)*v1.angulos[0][0])),(v1.magnitud1*math.cos((math.pi/180)*v1.angulos[0][1])),(v1.magnitud1*math.cos((math.pi/180)*v1.angulos[0][2]))]
        componentes_fuerza2=[(v1.magnitud2*math.cos((math.pi/180)*v1.angulos[0][3])),(v1.magnitud2*math.cos((math.pi/180)*v1.angulos[0][4])),(v1.magnitud2*math.cos((math.pi/180)*v1.angulos[0][5]))]
        resultante_vectorial=[componentes_fuerza1[0]+componentes_fuerza2[0],componentes_fuerza1[1]+componentes_fuerza2[1],componentes_fuerza1[2]+componentes_fuerza2[2]]
        magnitud_resultante=math.sqrt((resultante_vectorial[0]**2)+(resultante_vectorial[1]**2)+(resultante_vectorial[2]**2))
        lambda_resultante=[resultante_vectorial[0]/magnitud_resultante,resultante_vectorial[1]/magnitud_resultante,resultante_vectorial[2]/magnitud_resultante]
        angulos_directores=[(180/math.pi)*math.acos(lambda_resultante[0]),(180/math.pi)*math.acos(lambda_resultante[1]),(180/math.pi)*math.acos(lambda_resultante[2])]
        Resultados="Resultados:\nComponente en x: "+str(resultante_vectorial[0])+"\nComponente en y: "+str(resultante_vectorial[1])+"\nComponente en z: "+str(resultante_vectorial[2])+"\n\nMagnitud: "+str(magnitud_resultante)+"\nθx: "+str(angulos_directores[0])+"\nθy: "+str(angulos_directores[1])+"\nθz: "+str(angulos_directores[2])+"\n\nPara volver a realizar un cálculo cierra esta ventana \ny elije en la ventana principal"
        self.resultado_ihat=tkinter.Label(self.ventana, text=Resultados)
        self.resultado_ihat.grid(row=20, column=3)

#Hecho por Elian JAVIER CRUZ ESQUIVEL, ICC, CETYS UNIVERSIDAD