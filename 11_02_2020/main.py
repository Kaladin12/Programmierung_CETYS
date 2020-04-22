import smatphone, app, musica, fotos, configuracion
print("Bienvenido a tu smartphone. Debes realizar las siguientes configuraciones: ")
mismartphone=smatphone.telefono(input("Nombre de usuario: "), input("Pais: "),input("Activar el gps [y][n]: "),input("Nombre del dispositivo: "))
mimusica=musica.musica()
misfotos=fotos.foto()
#miconfig=configuracion.configuracion(mismartphone)
aplicaciones=app.aplicacion(mimusica,misfotos, mismartphone)
aplicaciones.elegir()
quit()