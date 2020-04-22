import random

class cuadricula:
    def __init__(self):
        self.matriz=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

    def crear_matriz(self):
        for i in range(16):
            for a in range(16):
                self.matriz[i].extend(self.letras[random.randrange(27)])