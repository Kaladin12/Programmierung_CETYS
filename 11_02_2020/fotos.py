import foto_individual
class foto:
    def __init__(self):
        self.albums=[]
        self.nombre_albums=[]
        self.fotos=[]
    
    def crear_foto(self, nombre='', tamanio='0 bytes'):
        minuevafoto=foto_individual.foto_individual(nombre,tamanio)
        nuevalista=[minuevafoto.nombre, minuevafoto.tamanio]
        self.fotos.append(nuevalista)

    def crear_album(self, nombre=''):
        self.nombre_albums.append(nombre)
        nuevalista=[]
        self.albums.append(nuevalista)
    
    def elegir_album(self, nombrefoto='', album=''):
        if album in self.nombre_albums:
            numero=self.nombre_albums.index(album)
            self.albums[numero].append(nombrefoto)
            print(nombrefoto+" agregada al album "+album)
        else:
            print("foto o album inexistentes.")

    def borrar_foto(self, nombre=''): #hacer que borre correctamente
        for i in self.fotos:
            if i[0]==nombre:
                numero=self.fotos.index(i)
                self.fotos.pop(numero)
                break
        for i in self.albums:
            if nombre in i:
                numero=self.albums.index(i)
                i.pop(numero)
    
    def vermisfotos(self, album=''):
        nuevalista=[]
        if album in self.nombre_albums:
            numero=self.nombre_albums.index(album)
            if len(self.albums[numero])>0:
                for i in self.albums[numero]:
                    nuevalista.append(i)
                contador=0
                for i in self.fotos:
                    if nuevalista[contador] in i[0]:
                        print('Nombre: '+i[0])
                        print('Tamaño: '+i[1])
                    contador=contador+1  
            else:
                print('No hay fotos en el album')    