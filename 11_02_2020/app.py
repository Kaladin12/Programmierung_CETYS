import fotos
import configuracion
import musica, smatphone
import os
import time
clear=lambda: os.system('cls')
class aplicacion:
    def __init__(self, musica, fotos, config):
        self.apps=['Musica', 'Fotos', 'Configuracion', 'Salir']
        self.musica=musica
        self.fotos=fotos
        miconfig=configuracion.configuracion(config)
        self.config=miconfig
    
    def elegir(self):
        while True:
            i=0
            for item in self.apps:
                print(str(i+1)+' '+item)
                i=i+1
            respuesta=int(input("Cual deseas: "))
            if respuesta==1:
                funciones=['Crear cancion', 'Crear lista de reproducción', 'Agregar canción a lista de reproducción', 'Reproducir', 'Pausar', 'Ver canciones en una lista de reproducción', 'Salir']
                #main musica
                contador=1
                while True:
                    clear()
                    for i in funciones:
                        print('['+str(contador)+']'+i)
                        contador=contador+1
                    respuesta=int(input("Cual desea elegir: "))
                    if respuesta==1:
                        self.musica.crear_cancion(input("Ingresa nombre de la canción: "),input("Ingresa cantante: "), int(input("Ingresa año: ")))
                    elif respuesta==2:
                        self.musica.crear_lista(input("Ingresa nombre de la lista: "))
                    elif respuesta==3:
                        print("Listas disponibles: ")
                        for i in self.musica.nombres_listas:
                            print(i)
                        self.musica.agregar_cancion(input("Canción que desea agregar: "), input("Lista a la que desea agregar la canción: "))
                    elif respuesta==4:
                        self.musica.reproducir(input("Que canción desea reproducir: "))
                    elif respuesta==5:
                        self.musica.pausar()
                    elif respuesta==6:
                        self.musica.verlista(input("Ingresa nombre de la lista: "))
                    else:
                        break
                    contador=1
                    time.sleep(2)
            elif respuesta==2:
                funciones=['Crear foto', 'Crear album de fotos', 'Agregar foto a un album', 'Borrar una foto', 'Ver datos de fotos', 'Salir']
                contador=1
                while True:
                    clear()
                    for i in funciones:
                        print('['+str(contador)+']'+i)
                        contador=contador+1
                    respuesta=int(input("Cual desea elegir: "))
                    if respuesta==1:
                        self.fotos.crear_foto(input('Introduce nombre de la foto: '), input('Introduce tamaño de la foto: '))
                    elif respuesta==2:
                        self.fotos.crear_album(input("Introduce nombre del album: "))
                    elif respuesta==3:
                        print("Albums disponibles: ")
                        for i in self.fotos.nombre_albums:
                            print(i)
                        self.fotos.elegir_album(input("Introduce nombre de la foto: "),input("Introduce nombre del album: "))
                    elif respuesta==4:
                        self.fotos.borrar_foto(input("Introduce nombre de la foto: "))
                    elif respuesta==5:
                        self.fotos.vermisfotos(input("Introduce nombre del album: "))
                    else:
                        break
                    contador=1
                    time.sleep(2)
            elif respuesta==3:
                regreso=self.config.editarconfig()
                if regreso=="5":
                    self.musica=musica.musica()
                    self.fotos=fotos.foto()
                    print("Bienvenido a tu smartphone. Debes realizar las siguientes configuraciones: ")
                    self.mismartphone=smatphone.telefono(input("Nombre de usuario: "), input("Pais: "),input("Activar el gps [y][n]: "),input("Nombre del dispositivo: "))
                    miconfig=configuracion.configuracion(self.mismartphone)
                    self.config=miconfig
            else:
                quit()