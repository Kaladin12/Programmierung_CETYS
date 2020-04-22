import tkinter
from tkinter import ttk, messagebox
import time, numpy, matplotlib.pyplot, math
from mpl_toolkits import mplot3d

class vector:
    def __init__(self, coordenadas, magnitud):
        self.coordenadas=[]
        self.lambdas=[]
        self.magnitud=0

primera_vez=True

class coord:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.title('Suma de vectores en 3D      CRUZ ESQUIVEL ELIAN JAVIER')
        self.ventana.minsize(640,480)
        self.which=False
        self.vetores=[]
        self.panel_dos_coordenadas=tkinter.PanedWindow(self.ventana)
        self.label_ingresa_magnitud=tkinter.Label(self.panel_dos_coordenadas, text="Ingrese magnitud del vector: ")
        self.caja_magnitud=tkinter.Entry(self.panel_dos_coordenadas)
        self.caja_x=tkinter.Entry(self.panel_dos_coordenadas,text='')
        self.caja_y=tkinter.Entry(self.panel_dos_coordenadas)
        self.caja_z=tkinter.Entry(self.panel_dos_coordenadas)
        self.label_vector_1=tkinter.Label(self.panel_dos_coordenadas,text="Vector 1: ")
        self.label_x=tkinter.Label(self.panel_dos_coordenadas, text="X1: ")
        self.label_y=tkinter.Label(self.panel_dos_coordenadas, text="Y1: ")
        self.label_z=tkinter.Label(self.panel_dos_coordenadas, text="Z1: ")
        self.label_vector_2=tkinter.Label(self.panel_dos_coordenadas,text="Vector 1: ")
        self.caja_x2=tkinter.Entry(self.panel_dos_coordenadas)
        self.caja_y2=tkinter.Entry(self.panel_dos_coordenadas)
        self.caja_z2=tkinter.Entry(self.panel_dos_coordenadas)
        self.label_x2=tkinter.Label(self.panel_dos_coordenadas, text="X2: ")
        self.label_y2=tkinter.Label(self.panel_dos_coordenadas, text="Y2: ")
        self.label_z2=tkinter.Label(self.panel_dos_coordenadas, text="Z2: ")
        self.boton_listo=ttk.Button(self.panel_dos_coordenadas,text='Listo', command=self.listo)

        self.panel_dos_coordenadas2=tkinter.PanedWindow(self.ventana)
        self.label_ingresa_magnitud_=tkinter.Label(self.panel_dos_coordenadas2, text="Ingrese magnitud del vector: ")
        self.caja_magnitud_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.caja_x_=tkinter.Entry(self.panel_dos_coordenadas2,text='')
        self.caja_y_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.caja_z_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.label_vector_1_=tkinter.Label(self.panel_dos_coordenadas2,text="Vector 2: ")
        self.label_x_=tkinter.Label(self.panel_dos_coordenadas2, text="X1: ")
        self.label_y_=tkinter.Label(self.panel_dos_coordenadas2, text="Y1: ")
        self.label_z_=tkinter.Label(self.panel_dos_coordenadas2, text="Z1: ")
        self.label_vector_2_=tkinter.Label(self.panel_dos_coordenadas2,text="Vector 2: ")
        self.caja_x2_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.caja_y2_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.caja_z2_=tkinter.Entry(self.panel_dos_coordenadas2)
        self.label_x2_=tkinter.Label(self.panel_dos_coordenadas2, text="X2: ")
        self.label_y2_=tkinter.Label(self.panel_dos_coordenadas2, text="Y2: ")
        self.label_z2_=tkinter.Label(self.panel_dos_coordenadas2, text="Z2: ")
        self.boton_listo_=ttk.Button(self.panel_dos_coordenadas2,text='Listo', command=self.listo)
        self.add()
        self.ventana.mainloop()

    def add(self):
        self.panel_dos_coordenadas.grid(row=10, column=0)
        self.label_ingresa_magnitud.grid(row=0, column=2)
        self.caja_magnitud.grid(row=0, column=5)
        self.label_vector_1.grid(row=5, column=2)
        self.caja_x.grid(row=6, column=5)
        self.caja_y.grid(row=7, column=5)
        self.caja_z.grid(row=8, column=5)
        self.label_x.grid(row=6, column=2)
        self.label_y.grid(row=7, column=2)
        self.label_z.grid(row=8, column=2)
        self.label_vector_2.grid(row=9, column=2)
        self.caja_x2.grid(row=10, column=5)
        self.caja_y2.grid(row=11, column=5)
        self.caja_z2.grid(row=12, column=5)
        self.label_x2.grid(row=10, column=2)
        self.label_y2.grid(row=11, column=2)
        self.label_z2.grid(row=12, column=2)
        self.boton_listo.grid(row=13, column=5)
        #vector 2
        self.panel_dos_coordenadas2.grid(row=10, column=8)
        self.label_ingresa_magnitud_.grid(row=0, column=2)
        self.caja_magnitud_.grid(row=0, column=5)
        self.label_vector_1_.grid(row=5, column=2)
        self.caja_x_.grid(row=6, column=5)
        self.caja_y_.grid(row=7, column=5)
        self.caja_z_.grid(row=8, column=5)
        self.label_x_.grid(row=6, column=2)
        self.label_y_.grid(row=7, column=2)
        self.label_z_.grid(row=8, column=2)
        self.label_vector_2_.grid(row=9, column=2)
        self.caja_x2_.grid(row=10, column=5)
        self.caja_y2_.grid(row=11, column=5)
        self.caja_z2_.grid(row=12, column=5)
        self.label_x2_.grid(row=10, column=2)
        self.label_y2_.grid(row=11, column=2)
        self.label_z2_.grid(row=12, column=2)
        self.boton_listo_.grid(row=13, column=5)
    
    def listo(self):
        global primera_vez
        if primera_vez:
            try:
                lista=[float(self.caja_x.get()),float(self.caja_y.get()),float(self.caja_z.get()),float(self.caja_x2.get()),float(self.caja_y2.get()),float(self.caja_z2.get())]
                vector1=vector(lista, float(self.caja_magnitud.get()))
                vector1.coordenadas.append(lista)
                vector1.magnitud=float(self.caja_magnitud.get())
                self.vetores.append(vector1)
                primera_vez=False
            except:
                messagebox.showinfo(message="Solo introducir números", title='Error')
        else:
            try:
                lista=[float(self.caja_x_.get()),float(self.caja_y_.get()),float(self.caja_z_.get()),float(self.caja_x2_.get()),float(self.caja_y2_.get()),float(self.caja_z2_.get())]
                vector2=vector(lista,float(self.caja_magnitud_.get()))
                vector2.coordenadas.append(lista)
                vector2.magnitud=float(self.caja_magnitud_.get())
                self.vetores.append(vector2)
                primera_vez=True
                #print(vetores[0].coordenadas,vetores[1].coordenadas)
            except:
                messagebox.showinfo(message="Solo introducir números", title='Error')
            self.dos_coordenadas(self.vetores[0],vector2)

    def dos_coordenadas(self,v1,v2):
        nuevos_valores_1=[v1.coordenadas[0][3]-v1.coordenadas[0][0], v1.coordenadas[0][4]-v1.coordenadas[0][1], v1.coordenadas[0][5]-v1.coordenadas[0][2]]
        nuevos_valores_2=[v2.coordenadas[0][3]-v2.coordenadas[0][0], v2.coordenadas[0][4]-v2.coordenadas[0][1], v2.coordenadas[0][5]-v2.coordenadas[0][2]]
        resultante1=math.sqrt((nuevos_valores_1[0]*nuevos_valores_1[0])+(nuevos_valores_1[1]*nuevos_valores_1[1])+(nuevos_valores_1[2]*nuevos_valores_1[2]))
        resultante2=math.sqrt((nuevos_valores_2[0]*nuevos_valores_2[0])+(nuevos_valores_2[1]*nuevos_valores_2[1])+(nuevos_valores_2[2]*nuevos_valores_2[2]))
        for i in range(3):
            nuevos_valores_1[i]=(nuevos_valores_1[i]/resultante1)*v1.magnitud
            nuevos_valores_2[i]=(nuevos_valores_2[i]/resultante2)*v2.magnitud
        v1.lambdas.append(nuevos_valores_1)
        v2.lambdas.append(nuevos_valores_2)
        resultante_fuerza_vectorial=[nuevos_valores_1[0]+nuevos_valores_2[0],nuevos_valores_1[1]+nuevos_valores_2[1],nuevos_valores_1[2]+nuevos_valores_2[2]]
        magnitud_resultante=math.sqrt((resultante_fuerza_vectorial[0]**2)+(resultante_fuerza_vectorial[1]**2)+(resultante_fuerza_vectorial[2]**2))
        lambda_resultante=[(resultante_fuerza_vectorial[0]/magnitud_resultante),(resultante_fuerza_vectorial[1]/magnitud_resultante),(resultante_fuerza_vectorial[2]/magnitud_resultante)]
        angulos_directores=[(180/math.pi)*math.acos(lambda_resultante[0]),(180/math.pi)*math.acos(lambda_resultante[1]),(180/math.pi)*math.acos(lambda_resultante[2])]
        Resultados="Resultados:\nComponente en x: "+str(resultante_fuerza_vectorial[0])+"\nComponente en y: "+str(resultante_fuerza_vectorial[1])+"\nComponente en z: "+str(resultante_fuerza_vectorial[2])+"\n\nMagnitud: "+str(magnitud_resultante)+"\nθx: "+str(angulos_directores[0])+"\nθy: "+str(angulos_directores[1])+"\nθz: "+str(angulos_directores[2])+"\n\nPara volver a realizar un cálculo cierra esta ventana \ny elije en la ventana principal"
        self.resultado_ihat=tkinter.Label(self.ventana, text=Resultados)
        self.resultado_ihat.grid(row=20, column=3)

#Hecho por Elian JAVIER CRUZ ESQUIVEL, ICC, CETYS UNIVERSIDAD