import numpy
class cancion:
    def __init__(self, cancion='', artista='', duracion=0):
        self.nombre=cancion
        self.artista=artista
        self.duracion=numpy.random.randint(low=1, high=5, size=1)
