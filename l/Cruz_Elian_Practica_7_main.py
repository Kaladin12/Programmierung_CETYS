class Usuario:
    def __init__(self):
        self.nombre=''
        self.ap_m=''
        self.ap_p=''
        self.fecha=''
        self.estado=''
        self.sexo=''
        self.curp=''

meses=['ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']
def generar_curp(claves, usuario):
    registros=open('Cruz_Elian_Practica_7_Registros.txt','a')
    vocales=['a','e','i','o','u']
    usuario.curp=usuario.ap_p[0]
    for i in usuario.ap_p[1:]:
        if i in vocales:
            usuario.curp+=i.upper()
            break
    usuario.curp+=usuario.ap_m[0].upper()
    usuario.curp+=usuario.nombre[0].upper()
    if len(usuario.fecha[1])<2:
        usuario.fecha[1]='0'+usuario.fecha
    usuario.curp+=str(usuario.fecha[2][-2:])+str(usuario.fecha[0])+str(usuario.fecha[1])+str(usuario.sexo)+usuario.estado.upper()
    for i in usuario.ap_p[1:]:
        if i not in vocales:
            usuario.curp+=i.upper()
            break
    for i in usuario.ap_m[1:]:
        if i not in vocales:
            usuario.curp+=i.upper()
            break
    for i in usuario.nombre[1:]:
        if i not in vocales:
            usuario.curp+=i.upper()
            break
    print(usuario.curp)
    if usuario.sexo=='H':
        sexo='Hombre'
    else:
        sexo='Mujer'
    mensaje=usuario.nombre+'    '+usuario.ap_p+'    '+usuario.ap_m+'    '+sexo+'    '+meses[int(usuario.fecha[0])-1]+'   '+usuario.fecha[1]+'    '+usuario.fecha[2]+'    '+usuario.estado+'\t'+usuario.curp+'\n'
    registros.write(mensaje)
    registros.close()
    
def datos_usuario(claves):
    miusuario=Usuario()
    miusuario.nombre=input('Ingresa tu nombre [e.g.: Elian Cruz Esquivel]: ')
    miusuario.fecha=[input('Ingresa MES de nacimiento [e.g.:FEB]: '),input('Ingresa DÍA de nacimiento [e.g.:05]: '), input('Ingresa AÑO de nacimiento [e.g.:1900]:')]
    if not(miusuario.fecha[0].upper() in meses):
        while not(miusuario.fecha[0].upper() in meses):
            miusuario.fecha=[input('FORMATO INCORRECTO\nIngresa MES de nacimiento [e.g.:FEB]: '),input('Ingresa DÍA de nacimiento [e.g.:05]: '), input('Ingresa AÑO de nacimiento [e.g.:1900]:')]
    miusuario.estado=input('Ingresa tu estado: ')
    miusuario.fecha[0]=str(meses.index(miusuario.fecha[0].upper())+1)
    if len(miusuario.fecha[1])<2:
        miusuario.fecha[1]='0'+miusuario.fecha[1]
    if len(miusuario.fecha[0])<2:
        miusuario.fecha[0]='0'+miusuario.fecha[0]
    if miusuario.estado.lower() in claves:
        miusuario.estado=claves[miusuario.estado.lower()]
    print(miusuario.fecha)
    miusuario.sexo=input('Ingresa tu sexo [H/M]: ').upper()
    if miusuario.sexo!='H' and miusuario.sexo!='M':
        while miusuario.sexo!='H' and miusuario.sexo!='M':
            miusuario.sexo=input('Sexo inválido\nIngresa tu sexo [H/M]: ')
    aux=[]
    cont=0
    for i in miusuario.nombre:
        if i==' ':
            aux.append(cont)
        cont+=1
    miusuario.ap_p=miusuario.nombre[aux[0]+1:]
    miusuario.ap_m=miusuario.nombre[aux[1]+1:].upper()
    diferencia=int(aux[1])-int(aux[0]-1)
    miusuario.ap_p=miusuario.ap_p[:diferencia]
    miusuario.ap_p=miusuario.ap_p[:-2].upper()
    miusuario.nombre=miusuario.nombre[:aux[0]].upper()
    generar_curp(claves, miusuario)

def main():
    claves={}
    Registros=open('Cruz_Elian_Practica_7_Registros.txt','a')
    Claves=open('Cruz_Elian_Practica_7_Claves de Entidades Federativas.txt','r')
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    cont=0
    while True:
        if cont>=32:
            break
        i=Claves.readline()
        index=i.index('-')
        abreviacion=i[index+1:]
        estado=i[:index].lower()
        abreviacion=abreviacion[:-1]
        claves[estado]=abreviacion
        cont+=1
    Registros.close()
    while True:
        datos_usuario(claves)
        continuar=input('Deseas calcular otro CURP? [y/n]: ')
        if continuar!='y' and continuar!='Y':
            break
main()
