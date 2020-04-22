import os
clear=lambda: os.system('cls')
import libro
import something
        
#while True:
#    biblioteca=[]
#    cuantos=input("cuantos libros quieres: ")
#    contador = 0
#    for _ in range(int(cuantos)):
#        print("Libro: "+str(contador+1))
#        milibro=libro.libros(input("Ingresa anio: "), input("Ingresa editorial: "), input("ingresa titulo: "), input("ingresa isbn: "), input("ingresa autor: "))
#        biblioteca.append(milibro)
#        contador+=1
#    contador=0
#    clear()
#    for i in biblioteca:
#        print("Libro: "+str(contador+1))
#        print("Año: "+str(i.anio))
#        print("Autor: "+str(i.autor))
#        print("Titulo: "+str(i.titulo))
#        print("ISBN: "+str(i.isbn))
#        print("Editorial: "+str(i.editorial))
#        contador+=1
#    quit()
milibro=libro.libros("2015","Ediciones B", "Oathbringer","15215452")
algo=something.biblioteca('Nombre')
algo.bla(milibro.titulo)