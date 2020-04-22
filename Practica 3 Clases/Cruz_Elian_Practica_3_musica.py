import Cruz_Elian_Practica_3_cancion as songs
import Cruz_Elian_Practica_3_reproductor as reproductor
class musica:
    def __init__(self):
        self.listas_reproduccion=[]
        self.nombres_listas=[]
        self.canciones=[]
        self.listas_reproduccion.append(self.canciones)
        self.nombres_listas.append("Todas las canciones")

    def agregar_lista(self, nombre=''):
        self.nombres_listas.append(nombre)
        nueva_lista=[]
        self.listas_reproduccion.append(nueva_lista)

    def remover_lista(self, lista=''):
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            self.nombres_listas.pop(numero)
            self.listas_reproduccion.pop(numero)
            print("Lista de reproducción borrada")
        else:
            print("Lista inexistente")
    
    def reproducir_lista(self, lista=''):
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            print(numero)
            primeracancion=self.listas_reproduccion[numero][0][0]
            mireproductor=reproductor.reproductor(primeracancion,self.listas_reproduccion[numero])
            mireproductor.main_reproductor()
            #print(self.listas_reproduccion[numero])
    
    def agregar_cancion(self, cancion='', artista=''):
        nueva_cancion=songs.cancion(cancion,artista)
        lista=[nueva_cancion.nombre, nueva_cancion.artista, nueva_cancion.duracion]
        self.listas_reproduccion[0].append(lista)
    
    def remover_cancion(self, cancion=''):
        canciones=self.listas_reproduccion[0]
        lista=[]
        for i in canciones:
            lista.append(i[0])
        if cancion in lista:
            indice=lista.index(cancion)
            self.listas_reproduccion[0].pop(indice)
            contador=0
            for i in self.listas_reproduccion:
                if cancion in i:
                    indice=i.index(cancion)
                    self.listas_reproduccion[contador].pop(indice)
                contador=contador+1

    def seleccionar_cancion(self, cancion='', lista=''):
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            contador=0
            for i in self.listas_reproduccion[0]:
                if cancion in i[0]:
                    indice=i[0].index(cancion)
                    self.listas_reproduccion[numero].append(self.listas_reproduccion[0][contador])
                    print(cancion+" agregada a la lista de reproduccion "+lista)
                    break
                contador=contador+1
    
    def reproducir_cancion(self, cancion):
        for i in self.listas_reproduccion[0]:
                if cancion in i[0]:
                    indice=i[0].index(cancion)
                    mireproductor=reproductor.reproductor(self.listas_reproduccion[0][0][indice],self.listas_reproduccion[0])
                    mireproductor.main_reproductor()

    def verlista(self, lista=''):
        nuevalista=[]
        if lista in self.nombres_listas:
            numero=self.nombres_listas.index(lista)
            for i in self.listas_reproduccion[numero]:
                nuevalista.append(i)
            contador=0
            for i in self.canciones:
                if nuevalista[contador][0] in i[0]:
                    print('Nombre: '+i[0])
                    print('Artista: '+i[1])
                    print('Duración: '+str(i[2][0]))
                if contador>=len(nuevalista):
                    break
               
                