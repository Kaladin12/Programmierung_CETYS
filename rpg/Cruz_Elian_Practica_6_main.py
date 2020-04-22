import numpy as np
from msvcrt import getch
from time import *
import Cruz_Elian_Practica_6_personajes as characters
import os, crayons
clear=lambda: os.system('cls')
jug=False

usuarios=[]
datos_personajes_para_seleccion=[]
datos_personajes_para_seleccion.append(characters.mage())
datos_personajes_para_seleccion.append(characters.demon())
datos_personajes_para_seleccion.append(characters.skeleton())
lista_personajes=[]

def seleccionar_personaje():
    personajes=['mage.txt','demon.txt','skeleton.txt']
    for i in range(3):
        with open(personajes[i]) as f:
            asciis = f.read().splitlines()
            lista_personajes.append(asciis)
    contador=0
    seleccion=True
    global jug
    while True:
        if seleccion:
            clear()
            print('Jugador ',int(jug)+1)
            print('Utiliza los UP y DOWN ARROW KEYS para cambiar de personaje a seleccionar\nPresiona ENTER para seleccionarlo')
            print('Selecciona el personaje que desees: ')
            print('Nombre: ', datos_personajes_para_seleccion[contador].name)
            for k in lista_personajes[contador]:
                print('|', end='')
                if contador==0:
                    print(crayons.red(k),end='')
                elif contador==1:
                    print(crayons.blue(k),end='')
                elif contador==2:
                    print(crayons.green(k),end='')
                print('|')
            seleccion=False
            print('Descripcion:')
            for i in datos_personajes_para_seleccion[contador].descripcion:
                print('|', end='')
                print(i,end='')
                if len(i)<80:
                    for k in range(80-len(i)):
                        print(' ',end='')
                print('|')
        key=ord(getch())
        if key==80:
            seleccion=True
            contador-=1
            if contador<0:
                contador=2
        elif key==72:
            seleccion=True
            contador+=1
            if contador>=3:
                contador=0
        elif key==13:
            if contador==0:
                usuarios.append(characters.mage())
            elif contador==1:
                usuarios.append(characters.demon())
            elif contador==2:
                usuarios.append(characters.skeleton())
            break
        sleep(.1)
    jug=True

def escoger_senda(jugador):
    eleccion=True
    contador=0
    senda_a_elegir=0
    while True:
        iteracion=0
        if eleccion:
            clear()
            print('Utiliza los UP y DOWN ARROW KEYS para cambiar de senda a seleccionar\nPresiona ENTER para seleccionarla')
            print('Es momento de que escojas la senda por la que deseas curarte\nLas sendas disponibles son:')
            for i in jugador.sendas:
                if iteracion==contador:
                    senda_a_elegir=iteracion
                    print(crayons.blue('Senda '), crayons.blue(i))
                else:
                    print('Senda: ',i)
                iteracion+=1
        tecla=ord(getch())
        if tecla==80:
            eleccion=True
            contador+=1
            if contador>=3:
                contador=0
        elif tecla==72:
            eleccion=True
            contador-=1
            if contador<0:
                contador=2
        elif tecla==13:
            return senda_a_elegir
        sleep(0.01)

def aplicar_movimientos(key, jugador, oponente):
    if jugador.name=='Ammanas, Lord of the High House of Shadow':
        if key=='Atacar':
            jugador.attack(jugador ,oponente)
        elif key=='Inmovilizar':
            jugador.inmovilizar(jugador,oponente)
            jugador.movimientos.pop(key)
        elif key=='Liberar Mastines de Sombra':
            jugador.liberar_mastines_de_sombra(oponente)
            jugador.movimientos.pop(key)
        elif key=='Curacion con senda':
            jugador.curacion_por_sendas(escoger_senda(jugador),jugador)
    elif jugador.name=='Anomander Rake, Son of Darkness, Lord of the High House of Death':
        if key=='Atacar':
            jugador.attack(jugador,oponente)
        elif key=='Desenvainar Dragnipur':
            jugador.movimientos.pop(key)
            jugador.desenvainar_Dragnipur(oponente)
        elif key=='Soletaken':
            jugador.movimientos.pop(key)
            jugador.convertise_soletaken(oponente)
        elif key=='Curacion con senda':
            jugador.curacion_por_sendas(escoger_senda(jugador),jugador)
        if jugador.envenenado:
            jugador.envenenado=int(jugador.envenenado*.97)
    elif jugador.name=='Onos T\'Oolan, the Stonesword':
        if key=='Atacar':
            jugador.attack(jugador,oponente)
        elif key=='Convertirse en Polvo':
            jugador.convertirse_en_polvo(oponente)
        elif key=='Hablar con los dioses':
            jugador.movimientos.pop(key)
            jugador.hablar_con_los_dioses(oponente)
        if jugador.envenenado:
            jugador.envenenado=int(jugador.envenenado*.97)
    if key=='Surrender':
        jugador.surrender(jugador,oponente)

def realizar_movs():
    usuario1=False
    while usuarios[0].life>0 and usuarios[1].life>0:
        seleccion=True
        contador=0
        limite=len(usuarios[int(usuario1)].movimientos)
        key_to_use=''
        while True:
            if seleccion:
                clear()
                print('Nombre: ', usuarios[int(usuario1)].name,'    Vida:',end='')
                usuarios[int(usuario1)].imprimir_vida(usuarios[int(usuario1)])
                for i in usuarios[int(usuario1)].ascii:
                    print('|', end='')
                    if int(usuario1)==0:
                        print(crayons.red(i),end='')
                    elif int(usuario1)==1:
                        print(crayons.blue(i),end='')
                    print('|')
                iteracion=0
                print('Utiliza los UP y DOWN ARROW KEYS para cambiar movimiento a seleccionar\nPresiona ENTER para seleccionarlo')
                print('Selecciona el movimiento que desees: ')
                for key in usuarios[int(usuario1)].movimientos:
                    if contador==iteracion:
                        key_to_use=key
                        print(crayons.blue(key),crayons.blue(': '),crayons.blue(usuarios[int(usuario1)].movimientos[key]))
                    else:
                        print(key,': ',usuarios[int(usuario1)].movimientos[key])
                    iteracion+=1
                seleccion=False
            tecla=ord(getch())
            if tecla==80:
                seleccion=True
                contador+=1
                if contador>=limite:
                    contador=0
            elif tecla==72:
                seleccion=True
                contador-=1
                if contador<0:
                    contador=limite-1
            elif tecla==13:
                aplicar_movimientos(key_to_use, usuarios[int(usuario1)],usuarios[int(not(usuario1))])
                break
            sleep(0.01)
        usuario1=not(usuario1)
        #usuarios[int(usuario1)].life-=20
    if usuarios[0].life<0:
        print('Gana ',usuarios[1].name)
    elif usuarios[1].life<0:
        print('Gana ',usuarios[0].name)

def main():
    print('Este juego está basado en la serie de novelas de fantasía épica llamada Malazan Book of the Fallen')
    print('Algunos nombres se encuentran en Español y otros en Inglés porque suenan mejor en uno u otro idioma')
    print('Las sendas son espacios mágicos solo disponibles para los mortales, las cuales les otorgan poderes\nespeciales como curación o cambiar de forma.')
    print('Los controles para todos los menús son los siguientes:\nUP ARROW KEY---Ir hacia arriba en un menú')
    print('DOWN ARROW KEY---Ir hacia abajo en un menú')
    print('ENTER---Escoger elemento')
    print('\n\nPresiona cualquier tecla para continuar')
    tecla=ord(getch())
    clear()
    for i in range(2):
        seleccionar_personaje()
    realizar_movs()
    continuar=input('Desea volver a jugar? [y][n]: ')
    if continuar=='y':
        usuarios.clear()
        main()
    
main()