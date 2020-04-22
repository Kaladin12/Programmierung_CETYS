import os, time, Cruz_Elian_Practica_3_reproductor as reproductor
clear=lambda: os.system('cls')

class aplicacion:
    def __init__(self, musica):
        self.musica=musica
    
    def elegir(self):
        funciones=['Crear lista de reproducción', 'Borrar lista de reproducción', 'Reproducir lista de reproducción', 'Crear canción', 'Borrar canción', 'Agregar canción a lista de reproducción', 'Reproducir canción','Ver canciones en una lista de reproducción', 'Salir']
        contador=1
        while True:
            clear()
            for i in funciones:
                print('['+str(contador)+']'+i)
                contador=contador+1
            respuesta=int(input("Cual desea elegir: "))
            clear()
            if respuesta==1:
                self.musica.agregar_lista(input("Ingresa nombre de la lista a crear: "))
            elif respuesta==2:
                print("Listas disponibles: ")
                for i in self.musica.nombres_listas:
                    print('-'+i)
                self.musica.remover_lista(input("Ingresa nombre de lista a borrar: "))
            elif respuesta==3:
                if len(self.musica.listas_reproduccion[0])<=0:
                    print('Aún no hay canciones')
                else:
                    print("Listas disponibles: ")
                    for i in self.musica.nombres_listas:
                        print('-'+i)
                    self.musica.reproducir_lista(input("Ingresa nombre de lista a reproducir: "))
            elif respuesta==4:
                self.musica.agregar_cancion(input("Nombre: "), input("Artista: "))
            elif respuesta==5:
                if len(self.musica.listas_reproduccion[0])<=0:
                    print('Aún no hay canciones')
                else:
                    self.musica.remover_cancion(input("Nombre de la canción a borrar: "))
            elif respuesta==6:
                if len(self.musica.listas_reproduccion[0])<=0:
                    print('Aún no hay canciones')
                else:
                    print('Canciones disponibles: ')
                    for i in self.musica.listas_reproduccion[0]:
                        print('-'+i[0])
                    cancion=input("Canción que desea agregar: ")
                    print("Listas disponibles: ")
                    for i in self.musica.nombres_listas:
                        print('-'+i)
                    listad=input("Lista a la que desea agregar la canción: ")
                    self.musica.seleccionar_cancion(cancion, listad)
            elif respuesta==7:
                if len(self.musica.listas_reproduccion[0])<=0:
                    print('Aún no hay canciones')
                else:
                    print('Canciones disponibles')
                    for i in self.musica.listas_reproduccion[0]:
                        print('-'+i[0])
                    self.musica.reproducir_cancion(input("Canción: "))
            elif respuesta==8:
                print("Listas disponibles: ")
                for i in self.musica.nombres_listas:
                    print('-'+i)
                self.musica.verlista(input("Que lista desea ver: "))
            else:
                break
            contador=1
            time.sleep(2)