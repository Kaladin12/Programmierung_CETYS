import numpy,csv, os, random, time, msvcrt
from colorama import *
from distutils.util import strtobool

clear = lambda: os.system('cls')
cambiar_color=False
class cuadro:
    def __init__(self):
        self.coordenadas_x=[]
        self.coordenadas_y=[]
        self.valor=[]
        self.valor=[self.valor.append(1) for i in range(12)]
        self.destapados=[]
        self.suma=0
        self.nivel=0
        self.anterior=0
        self.envenenado=False
        self.destapados=[False, False, False, False, False,False, False, False, False, False,False, False]

j1=cuadro()
j2=cuadro()
aux=cuadro()

def gotoxy(x,y):
    print("\033[%d;%dH"%(y+1,x+1), end="")

def imprimir_cuadro(x,y,color):
    if color==True:
        print(Fore.BLUE+"_______")
        gotoxy(x,y+1)
        i=0
        for i in range(3):
            gotoxy(x,y+i+1)
            print(Fore.BLUE+"|     |")
        gotoxy(x,y+i+1)
        print(Fore.BLUE+"------")
        color=False
    else:
        print(Fore.WHITE+"_______")
        gotoxy(x,y+1)
        i=0
        for i in range(3):
            gotoxy(x,y+i+1)
            print("|     |")
        gotoxy(x,y+i+1)
        print("------")

def imprimir_hexagono(x,y):
    gotoxy(x,y)
    print("  ____")
    gotoxy(x,y+1)
    print(" /    \\")
    gotoxy(x,y+2)
    print("|      |")
    gotoxy(x,y+3)
    print(" \\    /")
    gotoxy(x,y+4)
    print("  ----")

def Coordenadas():
    clear()
    x=16
    y=6
    j1.coordenadas_x.append(0)
    j1.coordenadas_y.append(10)
    j1.coordenadas_x.append(8)
    j1.coordenadas_y.append(8)
    j1.coordenadas_x.append(8)
    j1.coordenadas_y.append(13)
    j2.coordenadas_x.append(82)
    j2.coordenadas_y.append(10)
    j2.coordenadas_x.append(74)
    j2.coordenadas_y.append(8)
    j2.coordenadas_x.append(74)
    j2.coordenadas_y.append(13)
    for i in range(3,12):
        j1.coordenadas_x.append(x)
        j1.coordenadas_y.append(y)
        y+=5
        if i==5 or i==8:
            x+=8
            y=6
    #primer jugador
    #esto imprime los cuadros
    for i in range(12):
        gotoxy(j1.coordenadas_x[i],j1.coordenadas_y[i])
        imprimir_cuadro(j1.coordenadas_x[i],j1.coordenadas_y[i],False)
    #hexagono
    imprimir_hexagono(40,10)
    #segundo jugador
    x=66
    y=16
    for i in range(11,2,-1):
        j2.coordenadas_x.append(x)
        j2.coordenadas_y.append(y)
        y-=5
        if i==9 or i==6:
            x-=8
            y=16
    #esto imprime los cuadros
    for i in range(12):
        gotoxy(j2.coordenadas_x[i],j2.coordenadas_y[i])
        imprimir_cuadro(j2.coordenadas_x[i],j2.coordenadas_y[i],False)

def Mostrar_descubiertos():
    for i in range(1,12):
        if j1.destapados[i]:
            gotoxy(j1.coordenadas_x[i]+3, j1.coordenadas_y[i]+2)
            print(j1.valor[i])
    for i in range(1,12):
        if j2.destapados[i]:
            gotoxy(j2.coordenadas_x[i]+3, j2.coordenadas_y[i]+2)
            print(j2.valor[i])

def asignar_numeros():
    numeros=int(numpy.random.randint(low=1, high=18, size=1))
    for i in range(12):
        j1.valor[i]=int(numpy.random.randint(low=1, high=18, size=1))
    n=int(numpy.random.randint(low=1, high=12, size=1))
    j1.valor[n]=0    
    nuevos=j1.valor
    random.shuffle(nuevos)
    for n in range(12):
        j2.valor[n]=nuevos[n]
    random.shuffle(j2.valor)
    Coordenadas()
    Mostrar_descubiertos()
    for i in j1.destapados:
        i=False
    for i in j2.destapados:
        i=False

def ganadores():
    if j1.envenenado:
        j1.suma=int(j1.suma/2)
    if j2.envenenado:
        j2.suma=int(j2.suma/2)
    if j1.suma>j2.suma:
        return 0
    elif j2.suma>j1.suma:
        return 1
    else:
        return 2

def cargar_datos():
    archivo=open('Cruz_Elian_Practica_9_Calabozo_partidas_guardadas.csv','r',newline='\n')
    Leer=csv.reader(archivo)
    arreglo_aux=[]
    j1.coordenadas_x.clear()
    j2.coordenadas_x.clear()
    j1.coordenadas_y.clear()
    j2.coordenadas_y.clear()
    j1.valor.clear()
    j2.valor.clear()
    numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in Leer:
        arreglo_aux.append([ i[0], int(i[1]), [int(i[2]),int(i[3]),int(i[4]),int(i[5]),int(i[6]),int(i[7]),int(i[8]),int(i[9]),int(i[10]),int(i[11]),int(i[12]),int(i[13])],
        [int(i[14]),int(i[15]),int(i[16]),int(i[17]),int(i[18]),int(i[19]),int(i[20]),int(i[21]),int(i[22]),int(i[23]),int(i[24]),int(i[25])],
        [int(i[26]),int(i[27]),int(i[28]),int(i[29]),int(i[30]),int(i[31]),int(i[32]),int(i[33]),int(i[34]),int(i[35]),int(i[36]),int(i[37])],
        [bool(strtobool(str(i[38]))),bool(strtobool(str(i[39]))),bool(strtobool(str(i[40]))),bool(strtobool(str(i[41]))),bool(strtobool(str(i[42]))),bool(strtobool(str(i[43]))),bool(strtobool(str(i[44]))),bool(strtobool(str(i[45]))),bool(strtobool(str(i[46]))),bool(strtobool(str(i[47]))),bool(strtobool(str(i[48]))),bool(strtobool(str(i[49])))],
        int(i[50]),int(i[51]), bool(strtobool(str(i[52]))),
        [int(i[53]),int(i[54]),int(i[55]),int(i[56]),int(i[57]),int(i[58]),int(i[59]),int(i[60]),int(i[61]),int(i[62]),int(i[63]),int(i[64])],
        [int(i[65]),int(i[66]),int(i[67]),int(i[68]),int(i[69]),int(i[70]),int(i[71]),int(i[72]),int(i[73]),int(i[74]),int(i[75]),int(i[76])],
        [int(i[77]),int(i[78]),int(i[79]),int(i[80]),int(i[81]),int(i[82]),int(i[83]),int(i[84]),int(i[85]),int(i[86]),int(i[87]),int(i[88])],
        [bool(strtobool(str(i[89]))),bool(strtobool(str(i[90]))),bool(strtobool(str(i[91]))),bool(strtobool(str(i[92]))),bool(strtobool(str(i[93]))),bool(strtobool(str(i[94]))),bool(strtobool(str(i[95]))),bool(strtobool(str(i[96]))),bool(strtobool(str(i[97]))),bool(strtobool(str(i[98]))),bool(strtobool(str(i[99]))),bool(strtobool(str(i[100])))],
        int(i[101]),int(i[102]),bool(strtobool(str(i[103]))) ])
    nombres=[]
    for i in arreglo_aux:
        nombres.append(i[0])
    clear()
    if len(nombres)==0:
        print('No hay partidas guardadas!')
        time.sleep(1)
        return 0
    print('Las partidas disponibles son: ')
    for i in nombres:
        print(i)
    respuesta=input('Cual deseas?: ')
    if respuesta not in nombres:
        while respuesta not in nombres:
            clear()
            print('Las partidas disponibles son: ')
            for i in nombres:
                print(i)
            respuesta=input('Cual deseas?: ')
    clear()
    indice=nombres.index(respuesta)
    actual=arreglo_aux[indice][1]
    j1.coordenadas_x=arreglo_aux[indice][2]
    j1.coordenadas_y=arreglo_aux[indice][3]
    j1.valor=arreglo_aux[indice][4]
    j1.destapados=arreglo_aux[indice][5]
    j1.nivel=arreglo_aux[indice][6]
    j1.suma=arreglo_aux[indice][7]
    j1.envenenado=arreglo_aux[indice][8]
    j2.coordenadas_x=arreglo_aux[indice][9]
    j2.coordenadas_y=arreglo_aux[indice][10]
    j2.valor=arreglo_aux[indice][11]
    j2.destapados=arreglo_aux[indice][12]
    j2.nivel=arreglo_aux[indice][13]
    j2.suma=arreglo_aux[indice][14]
    j2.envenenado=arreglo_aux[indice][15]
    for i in range(12):
        gotoxy(j1.coordenadas_x[i],j1.coordenadas_y[i])
        imprimir_cuadro(j1.coordenadas_x[i],j1.coordenadas_y[i],False)
    for i in range(12):
        gotoxy(j2.coordenadas_x[i],j2.coordenadas_y[i])
        imprimir_cuadro(j2.coordenadas_x[i],j2.coordenadas_y[i],False)
    imprimir_hexagono(40,10)
    return int(actual)

def guardar_datos(actual):
    archivo=open('Cruz_Elian_Practica_9_Calabozo_partidas_guardadas.csv','a',newline='\n')
    Guardar=csv.writer(archivo)
    nombe=input('Con que nombre deseas guardar el archivo: ')
    for i in j1.destapados:
        try:
            if i==None or i==False:
                i='0'
            elif i==True:
                i='1'
        except:
            i='0'
    for i in j2.destapados:
        try:
            i=int(i)
        except:
            i=0
    Guardar.writerow([nombe, actual]+ j1.coordenadas_x+j1.coordenadas_y+j1.valor+j1.destapados+[(j1.nivel),(j1.suma),j1.envenenado]+j2.coordenadas_x+j2.coordenadas_y+j2.valor+j2.destapados+[(j2.nivel),(j2.suma),j2.envenenado])
    archivo.flush()

def mover_usuario(inicio):
    niveles=[[1,2,0],[3,4,5],[6,7,8],[9,10,11]]
    contador=inicio
    casilla_actual=0 #entre 0 y 2
    salir=False
    while contador<=8:
        suma=0
        nivel_actual=0
        if contador%2!=0:
            nivel_actual=j1.nivel
            suma=j1.suma
        else:
            nivel_actual=j2.nivel
            suma=j2.suma
        gotoxy(0,0)
        print('Puntuación: ',suma)
        key=ord(msvcrt.getch())
        if key==80:#key down
            casilla_actual-=1
            if casilla_actual<0:
                if nivel_actual==0:
                    casilla_actual=1
                else:
                    casilla_actual=2
            if contador%2!=0:
                for i in range(12):
                    gotoxy(j1.coordenadas_x[i],j1.coordenadas_y[i])
                    imprimir_cuadro(j1.coordenadas_x[i],j1.coordenadas_y[i],False)
                gotoxy(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]],j1.coordenadas_y[niveles[nivel_actual][casilla_actual]])
                imprimir_cuadro(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]],j1.coordenadas_y[niveles[nivel_actual][casilla_actual]],True)
            #gotoxy(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]]+3,j1.coordenadas_y[niveles[nivel_actual][casilla_actual]]+2)
            #print(j1.valor[niveles[nivel_actual][casilla_actual]])
            else:
                for i in range(12):
                    gotoxy(j2.coordenadas_x[i],j2.coordenadas_y[i])
                    imprimir_cuadro(j2.coordenadas_x[i],j2.coordenadas_y[i],False)
                Mostrar_descubiertos()
                gotoxy(j2.coordenadas_x[niveles[nivel_actual][casilla_actual]],j2.coordenadas_y[niveles[nivel_actual][casilla_actual]])
                imprimir_cuadro(j2.coordenadas_x[niveles[nivel_actual][casilla_actual]],j2.coordenadas_y[niveles[nivel_actual][casilla_actual]],True)
        elif key==72:
            casilla_actual+=1
            if (nivel_actual==0 and casilla_actual>1):
                casilla_actual=0
            elif (casilla_actual>2 and nivel_actual!=0):
                casilla_actual=0
            if contador%2!=0:
                for i in range(12):
                    gotoxy(j1.coordenadas_x[i],j1.coordenadas_y[i])
                    imprimir_cuadro(j1.coordenadas_x[i],j1.coordenadas_y[i],False)
                Mostrar_descubiertos()
                gotoxy(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]],j1.coordenadas_y[niveles[nivel_actual][casilla_actual]])
                imprimir_cuadro(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]],j1.coordenadas_y[niveles[nivel_actual][casilla_actual]],True)
            #gotoxy(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]]+3,j1.coordenadas_y[niveles[nivel_actual][casilla_actual]]+2)
            #print(j1.valor[niveles[nivel_actual][casilla_actual]])
            else:
                for i in range(12):
                    gotoxy(j2.coordenadas_x[i],j2.coordenadas_y[i])
                    imprimir_cuadro(j2.coordenadas_x[i],j2.coordenadas_y[i],False)
                gotoxy(j2.coordenadas_x[niveles[nivel_actual][casilla_actual]],j2.coordenadas_y[niveles[nivel_actual][casilla_actual]])
                imprimir_cuadro(j2.coordenadas_x[niveles[nivel_actual][casilla_actual]],j2.coordenadas_y[niveles[nivel_actual][casilla_actual]],True)
        elif key==27: 
            clear()
            gotoxy(0,0)
            print('Estas en el menú de pausa. Las opciones son: ')
            menu=['[1] Continuar','[2] Guardar y Salir','[3] Salir']
            for opcion in menu:
                print(opcion)
            respuesta=input('Qué deseas hacer?: ')
            if respuesta!='1' and respuesta!='2' and respuesta!='3':
                while respuesta!='1' and respuesta!='2' and respuesta!='3':
                    clear()
                    gotoxy(0,0)
                    print('Estas en el menú de pausa. Las opciones son: ')
                    menu=['[1] Continuar','[2] Guardar y Salir','[3] Salir']
                    for opcion in menu:
                        print(opcion)
                    respuesta=input('Qué deseas hacer?: ')
            if respuesta=='1':
                clear()
                for i in range(12):
                    gotoxy(j2.coordenadas_x[i],j2.coordenadas_y[i])
                    imprimir_cuadro(j2.coordenadas_x[i],j2.coordenadas_y[i],False)
                    gotoxy(j1.coordenadas_x[i],j1.coordenadas_y[i])
                    imprimir_cuadro(j1.coordenadas_x[i],j1.coordenadas_y[i],False)
                Mostrar_descubiertos()
                imprimir_hexagono(40,10)
            elif respuesta=='2':
                guardar_datos(contador)#Falta esto
                salir=True
                break
            else:
                salir=True
                break
        elif key==13:
            if contador%2!=0:
                j1.nivel+=1
                if j1.valor[niveles[nivel_actual][casilla_actual]]==0:
                    j1.envenenado=True
                    gotoxy(10,4)
                    print(Fore.LIGHTGREEN_EX+'JUGADOR 2 ENVENENADO!!!')
                    gotoxy(10,4)
                    print(Fore.WHITE+'                       ')
                    time.sleep(.85)
                j1.suma+=j1.valor[niveles[nivel_actual][casilla_actual]]
                j1.destapados[niveles[nivel_actual][casilla_actual]]=True
                gotoxy(j1.coordenadas_x[niveles[nivel_actual][casilla_actual]]+3,j1.coordenadas_y[niveles[nivel_actual][casilla_actual]]+2)
                print(j1.valor[niveles[nivel_actual][casilla_actual]])
            else:
                j2.nivel+=1
                if j2.valor[niveles[nivel_actual][casilla_actual]]==0:
                    j2.envenenado=True
                    gotoxy(10,4)
                    print(Fore.LIGHTGREEN_EX+'JUGADOR 2 ENVENENADO!!!')
                    gotoxy(10,4)
                    print(Fore.WHITE+'                       ')
                    time.sleep(.85)
                j2.suma+=j2.valor[niveles[nivel_actual][casilla_actual]]
                j2.destapados[niveles[nivel_actual][casilla_actual]]=True
                gotoxy(j2.coordenadas_x[niveles[nivel_actual][casilla_actual]]+3,j2.coordenadas_y[niveles[nivel_actual][casilla_actual]]+2)
                print(j2.valor[niveles[nivel_actual][casilla_actual]])
            contador+=1
        time.sleep(.1)
    if not salir:
        Mostrar_descubiertos()
        ganador=ganadores()
        gotoxy(0,0)
        print(Fore.GREEN+'Puntuacion jugador 1:', j1.suma)
        gotoxy(25,0)
        print(Fore.MAGENTA+'Puntuacion jugador 2:', j2.suma)
        print(Fore.WHITE+"")
        if ganador>=2:
            gotoxy(10,4)
            print(Fore.RED+'Empate')
        else:
            print(Fore.YELLOW+'Gana el jugador '+str(ganador+1)+', FELICIDADES!!!')
        l=input(Fore.WHITE+'Presiona enter para ir al menú')
    else:
        clear()
        gotoxy(0,0)
        print(Fore.WHITE+'Seras redirigido al menú principal')

def main():
    while True:
        clear()
        j1.__init__()
        j2.__init__()
        menu=['[1] Nueva Partida','[2] Cargar Una Partida','[3] Salir']
        gotoxy(0,0)
        print("Las especificaciones son las siguientes:\nSi la casilla elegida contiene un cero, el jugador que la eligio esta envenenado\nes decir, se le restan la mitad de sus puntos al final\n\nLos movimientos se hacen con las flechas arriba-abajo del teclado y enter para seleccionar.")
        print('Tienes las siguientes opciones: ')
        for i in menu:
            print(i)
        respuesta=input('Qué deseas hacer?: ')
        if respuesta!='1' and respuesta!='2' and respuesta!='3':
            while respuesta!='1' and respuesta!='2' and respuesta!='3':
                clear()
                gotoxy(0,0)
                print('Tienes las siguientes opciones: ')
                for opcion in menu:
                    print(opcion)
                respuesta=input('Qué deseas hacer?: ')
        if respuesta=='1':
            clear()
            asignar_numeros()
            mover_usuario(1)
        elif respuesta=='2':
            clear()
            inicio=cargar_datos()
            if inicio!=0:
                mover_usuario(inicio)
        else:
            print('Hasta pronto!!!')
            break
main()