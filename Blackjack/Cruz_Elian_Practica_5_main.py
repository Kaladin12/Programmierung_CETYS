import math, os,random,time
import Cruz_Elian_Practica_5_mazo as mazo
import Cruz_Elian_Practica_5_jugador as jugador
import Cruz_Elian_Practica_5_mano as mano
clear=lambda: os.system('cls')
def buscar_repetidos(mimazo):
    numero=random.randrange(52)
    if mimazo.elegidas[numero]==True:
        while mimazo.elegidas[numero]==True:
            numero=random.randrange(52)
    return numero

def obtener_suma(cartas_mano, jug):
    suma=0
    for i in cartas_mano:
        for n in i.cartas:
            if n[:1]=='K' or n[:1]=='Q' or n[:1]=='J' or n[:1]=='1':
                suma=suma+10
            elif n[:1]=='A':
                if suma+11>21:
                    suma+=1
                else:
                    suma+=11
            else:
                suma+=int(n[:1])
    return suma

def rendirse(jugadores,mimazo):
    jugadores[0].dinero-=jugadores[0].manos[0][0].apuesta*.5

def agregar_carta_a_manos(mimazo,jugadores):
    contador=0
    for i in jugadores[0].manos:
        numero=buscar_repetidos(mimazo)
        i[0].cartas.append(mimazo.cartas[numero])
        mimazo.elegidas[numero]=True
        i[0].suma=obtener_suma(i,jugadores[0].nombre)
        if contador==1:
            i[0].apuesta=float(input('Ingrese apuesta para nueva mano'))
        contador+=1
    if mimazo.casa_plantada==False:
        numero=buscar_repetidos(mimazo)
        jugadores[1].manos[0][0].cartas.append(mimazo.cartas[numero])
        mimazo.elegidas[numero]=True
        jugadores[1].manos[0][0].suma=obtener_suma(i,jugadores[0].nombre)

def doblar(jugadores,mimazo):
    apuesta=float(input('Introduce apuesta adicional'))
    if apuesta>jugadores[0].dinero:
        while apuesta>jugadores[0].dinero:
            apuesta=float(input('No tienes fondos\nIntroduce apuesta adicional'))
    jugadores[0].manos[0][0].apuesta+=apuesta
    agregar_carta_a_manos(mimazo,jugadores)

def separar(mimazo, jugadores, cual):
    jugadores[0].cantidad_manos+=1
    mimano=mano.mano()
    mimano.cartas.append(jugadores[0].manos[cual][0].cartas.pop(1))
    jugadores[0].manos.append([mimano])
    jugadores[0].manos[cual][0].suma=0
    agregar_carta_a_manos(mimazo,jugadores)

def asegurar(jugadores,mimazo):
    apuesta=float(input('Introduce apuesta adicional'))
    if apuesta>jugadores[0].dinero:
        while apuesta>jugadores[0].dinero:
            apuesta=float(input('No tienes fondos\nIntroduce apuesta adicional'))
    jugadores[0].manos[0][0].apuesta+=apuesta
    agregar_carta_a_manos(mimazo,jugadores)

def repartir_cartas(jugadores, primeravez,mimazo):
    if primeravez:
        for jug in range(2):
            jugadores[jug].cantidad_manos=1
            mimano=mano.mano()
            numero=buscar_repetidos(mimazo)
            mimano.cartas.append(mimazo.cartas[numero])
            mimazo.elegidas[numero]=True
            numero=buscar_repetidos(mimazo)
            mimano.cartas.append(mimazo.cartas[numero])
            mimazo.elegidas[numero]=True
            jugadores[jug].manos.append([mimano])
            jugadores[jug].manos[0][0].suma=obtener_suma(jugadores[jug].manos[0],jugadores[jug].nombre)
            del mimano
    else:
        if mimazo.casa_plantada==True:
            for i in range(jugadores[0].cantidad_manos):
                numero=buscar_repetidos(mimazo)
                jugadores[0].manos[i][0].cartas.append(mimazo.cartas[numero])
                mimazo.elegidas[numero]=True
                jugadores[0].manos[i][0].suma=obtener_suma(jugadores[0].manos[i],jugadores[0].nombre)
        else:
            for jug in range(2):
                for i in range(jugadores[jug].cantidad_manos):
                    numero=buscar_repetidos(mimazo)
                    jugadores[jug].manos[i][0].cartas.append(mimazo.cartas[numero])
                    mimazo.elegidas[numero]=True
                    jugadores[jug].manos[i][0].suma=obtener_suma(jugadores[jug].manos[i],jugadores[jug].nombre)
            #print(mimano.cartas)
def main():
    opciones=['[1] Continuar','[2] Continuar y Doblar','[3] Rendirse','[4] Plantarse','[5] Continuar y Separar','[6] Continuar y Asegurar']
    dieces=['1','J','Q','K']
    mimazo=mazo.mazo()
    random.shuffle(mimazo.cartas)
    primeravez=True
    jugadores=[]
    for i in range(2):
        minuevojugador=jugador.jugador(primeravez)
        jugadores.append(minuevojugador)
        primeravez=False
    while jugadores[0].dinero>0:
        primeravez=True
        doblando=False
        asegurando=False
        repartir_cartas(jugadores,True,mimazo)
        apuesta=float(input('Cuanto deseas apostar en esta ronda: '))
        if apuesta>jugadores[0].dinero:
            while apuesta>jugadores[0].dinero:
                apuesta=float(input('No tienes suficientes fondos\nCuanto deseas apostar en esta ronda: '))
        jugadores[0].manos[0][0].apuesta=apuesta
        while True:
            clear()
            print('Cartas de la casa: ')
            for i in range(len(jugadores[1].manos[0][0].cartas)-1):
                print(jugadores[1].manos[0][0].cartas[i],end=' ')
            print('Carta volteadas')
            #jugadores[0].manos[0][0].cartas[0])
            if jugadores[1].manos[0][0].suma>=17: #La casa sd planta aquí
                mimazo.casa_plantada=True
                print('La casa se ha plantado.')
            if jugadores[1].manos[0][0].suma==21 and asegurando:
                jugadores[0].dinero+=jugadores[0].manos[0][0].apuesta
                print('Has ganado, la casa obtuvo Blackjack!!!')
                break
            elif asegurando and jugadores[1].manos[0][0].suma!=21:
                jugadores[0].dinero-=jugadores[0].manos[0][0].apuesta
                print('Has perdido, la casa no obtuvo Blackjack')
                break
            print('Cartas de: ',jugadores[0].nombre)
            limite=jugadores[0].cantidad_manos
            bj=False
            quitar=[]
            for n_mano in range(limite):
                print('Mano ',n_mano,'  La apuesta es: ',jugadores[0].manos[n_mano][0].apuesta)
                for i in jugadores[0].manos[n_mano][0].cartas:
                    print(i,end=' ')
                print('\nTu suma es: ',jugadores[0].manos[n_mano][0].suma)
                if jugadores[0].manos[n_mano][0].suma>21:
                    print('Perdiste!!!')
                    jugadores[0].dinero-=jugadores[0].manos[n_mano][0].apuesta
                    if doblando or asegurando:
                        break
                    quitar.append(n_mano)
                elif jugadores[0].manos[n_mano][0].suma==21:
                    print('Blackjack!!!')
                    jugadores[0].dinero+=jugadores[0].manos[n_mano][0].apuesta
                    if doblando or asegurando:
                        break
                    else:
                        if jugadores[0].cantidad_manos>1:
                            quitar.append(n_mano)
                        else:
                            bj=True
                            break
            print('')
            if not(doblando or asegurando):
                if len(quitar)>0:
                    print(jugadores[0].manos)
                    for i in quitar:
                        jugadores[0].manos.pop(i)
                        jugadores[0].cantidad_manos-=1
            #print(jugadores[0].manos[0][0].cartas[0],jugadores[0].manos[0][0].cartas[1])
            #verifica las manos en busca de 21 o mas de 21
            #opciones=['[1] Continuar','[2] Continuar y Doblar','[3] Rendirse','[4] Plantarse','[5] Continuar y Separar','[6] Continuar y Asegurar']
                if jugadores[0].cantidad_manos<=0:
                    print('Te quedaste sin manos, has perdido!!!')
                    break
                if bj==True:
                    break
                dobla=-1
                print('Opciones: ')
                for i in range(jugadores[0].cantidad_manos):
                    if (jugadores[0].manos[i][0].cartas[0][:1]==jugadores[0].manos[i][0].cartas[1][:1]) or (jugadores[0].manos[i][0].cartas[0][:1] in dieces and jugadores[0].manos[i][0].cartas[1][:1] in dieces):
                        dobla=i
                        break
                if dobla!=-1:
                    if primeravez==True:
                        if jugadores[1].manos[0][0].cartas[0][:1]=='A':
                            for k in opciones:
                                print(k,end=' ')
                        else:
                            for k in opciones[:5]:
                                print(k,end=' ')
                    else:
                        print(opciones[0],' ',opciones[1],' ',opciones[3],' ',opciones[4])
                else:
                    if primeravez==True:
                        if jugadores[1].manos[0][0].cartas[0][:1]=='A':
                            for k in opciones[:4]:
                                print(k,end=' ')
                            print(opciones[5])
                        else:
                            for k in opciones[:4]:
                                print(k, end=' ')
                    else:
                        print(opciones[0],' ',opciones[1],' ',opciones[3])
                primeravez=False
                #print(quitar, jugadores[0].cantidad_manos,dobla)
                print('')
                respuesta=input('Que deseas hacer: ')
                if respuesta=='4':
                    print('Suma de la casa: ',jugadores[1].manos[0][0].suma)#,'   Suma de ',jugadores[0].nombre,': ',jugadores[0].manos[0][0].suma)
                    for i in range(jugadores[0].cantidad_manos):
                        print('i: ',i)
                        if (jugadores[1].manos[0][0].suma<=21 and jugadores[0].manos[i][0].suma<=21):
                            if jugadores[0].manos[i][0].suma>jugadores[1].manos[0][0].suma:
                                print('Gana ',jugadores[0].nombre)
                                jugadores[0].dinero+=jugadores[0].manos[i][0].apuesta
                            elif jugadores[1].manos[0][0].suma>jugadores[0].manos[0][0].suma:
                                print('Gana ',jugadores[1].nombre)
                                jugadores[0].dinero-=jugadores[0].manos[i][0].apuesta
                                break
                            else:
                                print('Empate')
                                break
                        else:
                            if jugadores[1].manos[i][0].suma>21 and jugadores[0].manos[i][0].suma<=21:
                                print('Gana ',jugadores[0].nombre)
                                jugadores[0].dinero+=jugadores[0].manos[i][0].apuesta
                                break
                            elif jugadores[0].manos[i][0].suma>21 and jugadores[1].manos[i][0].suma<=21:
                                print('Gana ',jugadores[1].nombre)
                                jugadores[0].dinero-=jugadores[0].manos[i][0].apuesta
                                break
                            else:
                                print('Empate')
                                break
                    break
                elif respuesta=='1':
                    repartir_cartas(jugadores,False,mimazo)
                elif respuesta=='2':
                    doblar(jugadores,mimazo)
                    doblando=True
                elif respuesta=='3':
                    rendirse(jugadores,mimazo)
                    print('Te has rendido')
                    break
                elif respuesta=='6':
                    asegurar(jugadores,mimazo)
                    asegurando=True
                elif respuesta=='5':
                    separar(mimazo, jugadores,dobla)
            else:
                break
        time.sleep(1.5)
        clear()
        print('El jugador ',jugadores[0].nombre,' tiene el siguiente dinero: $',jugadores[0].dinero)
        if jugadores[0].dinero>0:
            answ=input('Que deseas hacer: \n[1] Continuar\n[2] Salir\n')
            if not(answ=='1'):
                print('Gracias por visitar el Casino CETYS')
                time.sleep(2)
                break
            else:
                for i in jugadores:
                    i.manos.clear()
                    i.cantidad_manos=0
                mimazo=mazo.mazo()
        else:
            print('Gracias por visitar el Casino CETYS')
            time.sleep(2)
            break
main()