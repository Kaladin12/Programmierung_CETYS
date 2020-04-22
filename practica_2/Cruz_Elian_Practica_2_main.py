import Cruz_Elian_Practica_2_saludo as saludo
import Cruz_Elian_Practica_2_Geometria as Modulo_Geometria
import os
clear=lambda: os.system('cls')

while True:
    opcion=int(input("Que desea hacer: \n[1]--Saludo\n[2]--Geometría\n"))
    if opcion==1:
        saludo.saludar(input("Ingresa nombre: "))
        print(saludo.datos(input("Ingresa nombre: "), input("Ingresa Apellido: "), int(input("Ingresa año de nacimiento: "))))
    elif opcion==2:
        while True:
            respuesta=int(input("Que desea hacer: \n[1]--Area\n[2]--Volumen\n[3]--Salir"))
            clear()
            if respuesta>=3:
                quit()
            radio=int(input("Ingrese longitud del radio"))
            n_lados=int(input("Ingrese numero de lados (1 para círculo)"))
            area=Modulo_Geometria.area(radio, n_lados)
            
            if respuesta==1:
                print("El area es: "+str(area))
            elif respuesta==2:
                prisma=input("Desea \n[1]--Prisma\n[2]--Piramide")
                altura=float(input("Introduzca Altura: "))
                if prisma=="1":
                    print("El volumen es: "+str(Modulo_Geometria.volumen(area,True,altura)))
                elif prisma=="2":
                    resultado=Modulo_Geometria.volumen(area,False,altura)
                    print("El volumen es: "+str(resultado))
            else:
                quit()  