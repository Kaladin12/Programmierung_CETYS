import tkinter as tk
from tkinter import ttk
import json, csv

dia=0
anio=0
class Usuario:
    def __init__(self):
        self.nombre=''
        self.ap_m=''
        self.ap_p=''
        self.fecha=''
        self.sexo=''
        self.curp=''

def guardar_en_json(miUsuario, nombre):
    usuario={
        'nombre': nombre,
        'dia':str(dia.get()),
        'mes':comboMes.get(),
        'año':str(anio.get()),
        'estado':comboEstados.get(),
        'genero':comboGenero.get(),
        'curp':miUsuario.curp
    }
    User=json.dumps(usuario)
    with open('CURPS.json', 'a') as f:
        f.write(User)
        f.write('\n')
        f.close()

def Generar_CURP():
    global dia
    global anio
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    miusuario=Usuario()
    miusuario.nombre=name.get()
    miDia=str(dia.get())
    miMes=comboMes.current()+1
    if len(miDia)<2:
        miDia='0'+miDia
    if len(str(miMes))<2:
        miMes='0'+str(miMes)
    miusuario.fecha=miDia+miMes+str(anio)[-2:]
    aux=[]
    nombre=miusuario.nombre
    cont=0
    for i in miusuario.nombre:
        if i==' ':
            aux.append(cont)
        cont+=1
    miusuario.ap_p=miusuario.nombre[aux[0]+1:]
    miusuario.ap_m=miusuario.nombre[aux[1]+1:].upper()
    diferencia=int(aux[1])-int(aux[0]-1)
    miusuario.ap_p=miusuario.ap_p[:diferencia]
    miusuario.ap_p=miusuario.ap_p[:-2].upper()
    miusuario.nombre=miusuario.nombre[:aux[0]].upper()

    vocales=['a','e','i','o','u']
    miusuario.curp=miusuario.ap_p[0]
    for i in miusuario.ap_p[1:].lower():
        if i in vocales:
            miusuario.curp+=i.upper()
            break
    miusuario.curp+=miusuario.ap_m[0].upper()
    genro='H' if comboGenero.current()==0 else 'M'
    miusuario.curp+=miusuario.nombre[0].upper()+str(anio.get())[-2:]+miMes+miDia+genro+misClaves[comboEstados.get()]
    for i in miusuario.ap_p[1:]:
        if i not in vocales:
            miusuario.curp+=i.upper()
            break
    for i in miusuario.ap_m[1:]:
        if i not in vocales:
            miusuario.curp+=i.upper()
            break
    for i in miusuario.nombre[1:]:
        if i not in vocales:
            miusuario.curp+=i.upper()
            break
    miusuario.curp+='A1'
    guardar_en_json(miusuario, nombre)
    
def main():
    claves={}
    f=open('Cruz_Elian_Practica_10_Claves de Entidades Federativas.csv','r', newline='\n')
    Claves = csv.reader(f)
    for i in Claves:
        claves[i[0].lower()]=i[1]
    return claves

window=tk.Tk()
window.geometry('600x240')
misClaves=main()
solo_nombres=[]
for i in misClaves:
    solo_nombres.append(i)

myLabel_1=tk.Label(master=window, text='Este es un programa para obtener tu CURP')
myLabel_1.grid(column=0, row=0)

comboEstados=ttk.Combobox(master=window, state="readonly")
comboEstados['values']=solo_nombres
comboEstados.current(0)
comboEstados.grid(column=2, row=1)

myLabel = tk.Label(master=window, text="Escoge tu estado: " )
myLabel.grid(column=0, row=1)

name=tk.StringVar()
myText_Name=tk.Entry(window, width=24, textvariable=name)
myText_Name.grid(column=2, row=3)

myLabel = tk.Label(master=window, text="Ingresa tu nombre: [primer nombre y tus apellidos] " )
myLabel.grid(column=0, row=3)

dia=tk.IntVar()
anio=tk.IntVar()
myText_dia=tk.Entry(window, width=24, textvariable=dia)
myText_dia.grid(column=2, row=4)
myLabel = tk.Label(master=window, text="Ingresa tu dia de nacimiento: " )
myLabel.grid(column=0, row=4)

comboMes=ttk.Combobox(master=window, state="readonly")
comboMes['values']=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
comboMes.current(0)
comboMes.grid(column=2, row=5)

myLabel = tk.Label(master=window, text="Escoge tu mes de nacimiento: " )
myLabel.grid(column=0, row=5)

myText_anio=tk.Entry(window, width=24, textvariable=anio)
myText_anio.grid(column=2, row=6)
myLabel = tk.Label(master=window, text="Ingresa tu año de nacimiento: " )
myLabel.grid(column=0, row=6)

comboGenero=ttk.Combobox(master=window, state="readonly")
comboGenero['values']=['Hombre','Mujer']
comboGenero.current(0)
comboGenero.grid(column=2, row=7)

myLabel = tk.Label(master=window, text="Escoge tu género: " )
myLabel.grid(column=0, row=7)

botonCURP = tk.Button(window, text="Obtener CURP", command=Generar_CURP)
botonCURP.grid(column=1, row=8)
window.mainloop()
