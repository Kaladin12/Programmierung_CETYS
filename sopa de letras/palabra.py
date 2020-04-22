class word:
    def __init__(self, longitud,txt):
        self.coordenadas=[]
        self.longitud=longitud        
        self.texto=txt
        self.desgloce=[char for char in self.texto]
        self.disposicion=""