import math, random,time,marco,os,usuario,palabra,cuadricula
from numpy import loadtxt

palabras = loadtxt('palabras.txt',dtype=str, delimiter=",")
lista_palabras=[]
palabras_utilizadas=[]
casillas_ocupadas=[]
for a in range(16*16):
    casillas_ocupadas.append(False)
clear=lambda: os.system('cls')
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

def imprimir_marco(matriz,usuario):
    print("Usuario: "+str(usuario.nombre)+"          Puntos: "+str(usuario.puntuacion))
    contador=0
    mimarco.extremos()
    for i in  range(16):
        if contador<10:
            print('0'+str(contador),end=" ")
        else:
            print(str(contador),end=" ")
        mimarco.lados()
        for a in  range(16):
            print(matriz[i][a],end="  ")
        mimarco.lados()
        print("")
        contador=contador+1
    mimarco.extremos()

def cargar_palabras():
    for i in palabras:
        nueva_palabra=palabra.word(len(i),i)
        lista_palabras.append(nueva_palabra)
    random.shuffle(lista_palabras)

def diagonales(num_palabra,palabra_actual):
    print('')

#reverse
def posicionar_palabras(cuadricula):
    for i in lista_palabras:
        i.coordenadas.append(random.randrange(15))
        i.coordenadas.append(random.randrange(15))
    for i in lista_palabras:
        numero_palabra=0
        if 13-i.coordenadas[0]>=i.longitud:
            contador=0
            for a in range(i.longitud):
                print(str(a), i.texto, i.longitud, str(contador), i.coordenadas[0],i.coordenadas[1],i.desgloce)
                cuadricula.matriz[i.coordenadas[0]+contador][i.coordenadas[1]]=i.desgloce[contador]
                contador=contador+1
        elif 13-i.coordenadas[1]>=i.longitud:
            contador=0
            for a in range(i.longitud):
                print(str(a), i.texto, i.longitud, str(contador), i.coordenadas[0],i.coordenadas[1],i.desgloce)
                cuadricula.matriz[i.coordenadas[0]][i.coordenadas[1]+contador]=i.desgloce[contador]
                contador=contador+1
        elif i.coordenadas[1]+2>=i.longitud:
            contador=0
            for a in range(i.longitud):
                cuadricula.matriz[i.coordenadas[0]][i.coordenadas[1]-contador]=i.desgloce[contador]
                contador=contador+1
        elif i.coordenadas[0]+2>=i.longitud:
            contador=0
            for a in range(i.longitud):
                cuadricula.matriz[i.coordenadas[0]-contador][i.coordenadas[1]]=i.desgloce[contador]
                contador=contador+1
        else:
            diagonales(numero_palabra, i)
        numero_palabra=numero_palabra+1
        if numero_palabra>=10:
            break

os.system('mode 120,80')
mimarco=marco.marco()
while True:
    m_usuario=input("Ingrese su nombre de usuario: ")
    nuevo_usuario=usuario.usuario(m_usuario)
    micuadricula=cuadricula.cuadricula()
    micuadricula.crear_matriz()
    imprimir_marco(micuadricula.matriz,nuevo_usuario)
    cargar_palabras()
    posicionar_palabras(micuadricula)
    print(micuadricula.matriz)
    clear()
    imprimir_marco(micuadricula.matriz,nuevo_usuario)
    '''
    m_usuario=input("Ingrese su nombre de usuario: ")
    nuevo_usuario=usuario.usuario(m_usuario)
    clear()
    crear_matriz()
    imprimir_marco(nuevo_usuario)'''
    #posicionar_palabras()
    time.sleep(60)
    clear()
