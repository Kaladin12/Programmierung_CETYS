class telefono:
    def __init__(self, usuario='', pais='', gps='',n_dispositivo=''):
        self.usuario=usuario
        self.pais=pais
        if gps=='y':
            self.gps=True
        else:
            self.gps=False
        self.n_dispositivo=n_dispositivo

