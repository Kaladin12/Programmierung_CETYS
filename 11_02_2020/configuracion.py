class configuracion:
    def __init__(self, configuracion):
        self.configuracion=[configuracion.usuario,configuracion.pais, configuracion.gps, configuracion.n_dispositivo]

    def editarconfig(self):
        respuesta=''
        while True:
            print("Tus datos son: \n[1] Nombre usuario: "+self.configuracion[0]+"\n[2] País: "+self.configuracion[1]+"\n[3] GPS: "+str(self.configuracion[2])+"\n[4] Nombre del dispositivo: "+self.configuracion[3]+"\n[5] Configuración de fábrica\n[6] Regresar")
            respuesta=input("Cuál desea modificar: ")
            if respuesta=="1":
                self.configuracion[0]=input("Ingresa nuevo nombre de usuario: ")
            elif respuesta=="2":
                self.configuracion[1]=input("Ingresa nuevo País: ")
            elif respuesta=="3":
                gps=input("Ingresa gps [y][n]: ")
                if gps=="y":
                    self.configuracion[2]=True
                else:
                    self.configuracion[2]=False
            elif respuesta=="4":
                self.configuracion[3]=input("Ingresa nuevo nombre del dispositivo: ")
            elif respuesta=="5":
                self.configfabrica()  
            else:
                break
            return respuesta

    def configfabrica(self):
        print("")
