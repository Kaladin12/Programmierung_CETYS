import time, os, keyboard,msvcrt
clear=lambda: os.system('cls')
class reproductor:
    def __init__(self, cancion_actual, lista):
        self.cancion_actual=cancion_actual
        self.lista_canciones=lista
        self.indice=0
        contador=0
        for i in self.lista_canciones:
            if self.cancion_actual in i[0]:
                self.indice=contador
                break
            contador=contador+1                
    
    def main_reproductor(self):
        #Thread(target = self.reproducir).start()
        self.reproducir()

    def reproducir(self):
        iramenu=False
        opciones=['[1] Pausa', '[2] Siguiente', '[3] Anterior','[4] Regresar']
        print('Reproduciendo: '+self.lista_canciones[self.indice][0])
        while self.indice<len(self.lista_canciones) and iramenu==False:
            tiempo=self.lista_canciones[self.indice][2]
            contador=0
            for a in range(tiempo[0]*10):
                print('Reproduciendo: '+self.lista_canciones[self.indice][0])
                print('Tiempo:0'+str(contador+1))
                for i in opciones:
                    print(i)
                if msvcrt.kbhit():
                    respuesta = msvcrt.getch()
                    if str(respuesta)=='b\'1\'':
                        self.pausa()
                    elif str(respuesta)=='b\'2\'':
                        self.siguiente_pista()
                    elif str(respuesta)=='b\'3\'':
                        self.anterior_pista()
                    else:
                        iramenu=True
                        break
                time.sleep(0.1)
                if a/10==1 or a/10==2 or a/10==3 or a/10==4 or a/10==5:
                    contador=contador+1
                clear()
            self.indice=self.indice+1
            
    def pausa(self):
        tipo=-1
        clear()
        opciones=['En Pausa','[1] Reproducir', '[2] Siguiente', '[3] Anterior']
        for i in opciones:
            print(i)
        respuesta=input('Que deseas: ')
        if respuesta=="1":
            tipo=0
        elif respuesta=="2":
            tipo=1
        elif respuesta=="3":
            tipo=2
        time.sleep(0.1)
        print(tipo)
        if tipo==0:
            print('')
        elif tipo==1:
            self.siguiente_pista()
        elif tipo==2:
            self.anterior_pista()
    
    def siguiente_pista(self):
        self.indice=self.indice+1
        if self.indice>=len(self.lista_canciones):
            self.indice=self.indice-1
            print("No hay mas canciones en la lista")
        self.reproducir()
    
    def anterior_pista(self):
        self.indice=self.indice-1
        if self.indice<0:
            self.indice=self.indice+1
            print("Estas en la primer canción")
        self.reproducir()
    
    def salir(self):
        print('')
