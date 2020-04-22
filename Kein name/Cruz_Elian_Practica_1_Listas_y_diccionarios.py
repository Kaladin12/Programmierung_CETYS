#Hecho por Elian Javier Cruz Esquivel
import os
clear=lambda: os.system('cls')
saludo="Bienvenidos a Barnes & Noble"
salir=False
opciones=["[1] Comprar","[2] Ver Carrito","[3] Configuracion","[4] Salir"]
inicio=["[1] Iniciar Sesion","[2] Registrarse","[3] Salir"]
usuarios={"Usuario":"Elian",   "Ciudad":"Tijuana",    "Estado":"Baja California",    "Dia":"13",    "Mes":"04",    "Ano":"2001",    "Pago":"VISA",    "Psswrd":"0123456789123456",    "Mes_Pago":"01",    "Ano_Pago":"2019"}
articulos={0:"Illusions perdues  $250",1:"Oathbringer  $500",2:"The Final Empire  $450",3:"The three body problem  $260",4:"The moon is a hadr mistress  $350",5:"Dune  $370",6:"Gardens of the moon  $650",7:"The whisperer in darkness  $300"}
carrito_articulos=[]
carrito_cuantos=[]
comprados_contador=0

def Registro():
    usuarios["Usuario"]=input("Ïntroduzca su nombre de usuario: ")
    usuarios["Ciudad"]=input("Introduce Ciudad: ")
    usuarios["Estado"]=input("Introduce Estado: ")
    usuarios["Dia"]=input("Intrduce Dia de Nacimiento (dos cifras): ")
    usuarios["Ano"]=input("Introduce ano de nacimiento: ")
    usuarios["Mes"]=input("Introduce Mes de nacimiento (dos cifras): ")
    usuarios["Pago"]=input("Introduce Metodo de pago (VISA/MASTERCARD/AMEX): ")
    usuarios["Psswrd"]=input("Numero de tu tarjeta: ")
    usuarios["Mes_Pago"]=input("Mes de expiracion de tarjeta: ")
    usuarios["Ano_Pago"]=input("Ano de expiracion de tu tarjeta: ")

def LogIn():
    clear()
    entrada=input("Introduce tu usuario (escribe 0 para ir a pagina de registro): ")
    if entrada!="0":
        while True:
            if entrada==usuarios["Usuario"]:
                break
            else:
                print("Inexistente!!!, será redirigido a registro")
                entrada=input("Introduce tu usuario (escribe 0 para ir a pagina de registro): ")

    else:
        Registro()
        LogIn()

def Comprar():
    clear()
    print(saludo)
    global comprados_contador
    ir_a_carrito=False
    while True:
        for i in range(8):
            print("Articulo: "+str(i+1)+": "+articulos[i])
        carrito_articulos.append(str(int(input("introduce el articulo a elegir: "))-1))
        carrito_cuantos.append(int(input("Cuantos deseas comprar: ")))
        comprados_contador=comprados_contador+1
        salir=input("Que desea hacer? [1]-Ir a menu  [2]-Continuar  [3]-Ver Carrito")
        if salir=="1":
            break
        elif salir=="3":
            ir_a_carrito=True
            break
        clear()
    clear()
    if ir_a_carrito:
        Carrito()

def Carrito():
    suma=0
    clear()
    print(saludo)
    global comprados_contador
    if len(carrito_cuantos)<=0:
        print("No hay articulos en el carrito")
    else:
        for i in range(comprados_contador):
            art=int(articulos[i][-3:])
            suma=suma+(art*int(carrito_cuantos[i-1]))
            print(str(articulos[i])+"  Cantidad:"+str(carrito_cuantos[i-1])+" Precio Total: "+str(int(art)*int(carrito_cuantos[i-1])))
        print("Total a pagar: $"+str(suma))
        pagar=input("Que desea hacer?\n[1]--Ir a Menu\n[2]--Pagar")
        if pagar=="2":
            clear()
            for i in range(comprados_contador):
                carrito_articulos.pop()
                carrito_cuantos.pop()
                comprados_contador=0
            print(saludo)
            print("Su compra fue exitosa!\nSe cargaron $"+str(suma)+"a su tarjeta "+usuarios["Pago"]+" con número "+usuarios["Psswrd"])
        else:
            clear()

def Configuracion():
    print("Información Personal\n---------------------------------------\nUsuario: "+usuarios["Usuario"]+
    "\nUbicación: "+usuarios["Ciudad"]+", "+usuarios["Estado"]+"\nFecha de Nacimiento: "+usuarios["Dia"]+"/"+usuarios["Mes"]+"/"+usuarios["Ano"] )
    print("\nMétodo de Pago\n---------------------------------------\n"+usuarios["Pago"]+"\n"+usuarios["Psswrd"]+"\nFecha de expiración: "+usuarios["Mes_Pago"]+"/"+usuarios["Ano_Pago"])
    salir=input("Pulse cualquier tecla para regresar al menú")
    clear()

while True:
    for i in inicio:
        print(i)
    respuesta=input()

    if respuesta=="1":
        LogIn()
        break
    elif respuesta=="2":
        Registro()
        LogIn()
        clear()
        break
    elif respuesta=="3":
        quit()
    else:
        clear()

while True:
    for i in opciones:
        print(i)
    respuesta=input()
    if respuesta=="1":
        Comprar()
    elif respuesta=="2":
        Carrito()
    elif respuesta=="3":
        Configuracion()
    elif respuesta=="4":
        quit()
    else:
        clear()
