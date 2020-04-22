import math
def area(radio, n_lados):
    if n_lados==1:
        return math.pi*radio*radio
    else:
        angulo=((360/n_lados)/2)
        apotema=radio*math.cos(angulo*(math.pi/180))
        lado=2*radio*math.sin(angulo*(math.pi)/180)
        return ((n_lados*lado)*apotema/2)


def volumen(area_base,Tipo, Altura):
    if Tipo==True:
        return area_base*Altura
    else:
        return area_base*Altura/3