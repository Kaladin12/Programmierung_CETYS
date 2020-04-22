import songs
class musica:
    def __init__(self):
        self.listas_reproduccion=[]
        self.nombres_listas=[]
        self.canciones=[]
        self.actual=''

    def crear_cancion(self, cancion='', artista='',anio=''):
        nueva_cancion=songs.cancion(cancion,artista,int(anio))
        lista=[nueva_cancion.nombre, nueva_cancion.artista, nueva_cancion.anio]
        self.canciones.append(lista)

    def crear_lista(self, nombre=''):
        self.nombres_listas.append(nombre)
        nueva_lista=[]
        self.listas_reproduccion.append(nueva_lista)
    
    def agregar_cancion(self, cancion='', lista=''):
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            #comprobar si existe cancion
            self.listas_reproduccion[numero].append(cancion)
            print(cancion+" agregada a la lista de reproduccion "+lista)
        else:
            print("Lista o canción inexistente")
    
    def reproducir(self, cancion):
        for i in self.canciones:
            if i.nombre==cancion:
                self.actual=cancion
                print("Reproduciendo "+cancion)
                break

    def pausar(self):
        print("En Pausa: "+self.actual)

    def verlista(self, lista=''):
        nuevalista=[]
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            for i in self.listas_reproduccion[numero]:
                nuevalista.append(i)
            contador=0
            for i in self.canciones:
                if nuevalista[contador] in i[0]:
                    print('Nombre: '+i[0])
                    print('Artista: '+i[1])
                    print('Año: '+str(i[2]))
                if contador>=len(nuevalista):
                    break
                