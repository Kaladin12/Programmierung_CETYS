class jugador:
    def __init__(self , cpu):
        self.manos=[]
        self.cantidad_manos=0
        if cpu==True:
            self.nombre=input('Ingrese su nombre de usuario: ')
            self.dinero=int(input('Ingresa dinero a utilizar: '))
        else:
            self.nombre='cpu'