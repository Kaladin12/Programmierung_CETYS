import numpy as np
import crayons
from time import sleep
from tkinter import messagebox
class personaje:
    def __init__(self,which):
        personajes=['mage.txt','demon.txt','skeleton.txt']
        with open(personajes[which]) as f:
            self.ascii = f.read().splitlines()
        self.name=''
        self.life=25
        self.n_attack=0
        self.heal=0
        self.descripcion=''
    
    def attack(self,jugador,oponente):
        oponente.life-=abs(jugador.n_attack-oponente.heal)

    def imprimir_vida(self, pers):
        vida_rest=int(pers.life/2.5)
        print('|', end='')
        for i in range(vida_rest):
            #print(u'\u2764'
            print(crayons.red(u'\u2764'),end=' ')
        if vida_rest<10:
            for i in range(10-vida_rest):
                print(' ',end='')
        print('|')

    def surrender(self,jugador,oponente):
        print('')

class mortales:
    def __init__(self):
        self.sendas=['Del caos', 'Kurald Galain', 'De las sombras']
        self.visitas=0
    
    def curacion_por_sendas(self, cual, pers):
        aumento_correcto=1.2
        aumento_normal=1.15
        if self.visitas>0:
            aumento_normal=int(aumento_normal*(1-(.01*self.visitas)))
            aumento_correcto=int(aumento_correcto**(1-(.01*self.visitas)))
        print('Has ingresado a la senda, te protege de daños y magia')
        #messagebox.showinfo('',str(pers.life)+' '+str(pers.life*1.2))
        if pers.name=='Ammanas, Lord of the High House of Shadow':
            if cual==2:
                pers.life=int(pers.life*aumento_correcto)
            else:
                pers.life=int(pers.life*aumento_normal)
        elif pers.name=='Anomander Rake, Son of Darkness, Lord of the High House of Death':
            if cual==1:
                pers.life=int(pers.life*aumento_correcto)
            else:
                pers.life=int(pers.life*aumento_normal)
        if pers.life>25:
            pers.life=25
        self.visitas+=1
        sleep(1)

class mage(personaje, mortales):
    def __init__(self):
        personaje.__init__(self,0)
        mortales.__init__(self)
        self.name='Ammanas, Lord of the High House of Shadow'
        self.n_attack=4
        self.heal=2
        self.movimientos={'Atacar':'Daño: 4', 'Inmovilizar':'Envenenar a tus enemigos\n    -3% de Vida para enemigos cada turno', 'Liberar Mastines de Sombra':'Despedazan a los enemigos con sus mordidas\n+25% de Ataque', 'Curacion con senda':'Accede a tu senda para curarte\nSe recomienda escoger la Senda de las Sombras'}
        self.descripcion=['Conocido como Señor de la Gran Casa de las Sombras, es el mas poderoso','mago del mundo conocido, tiene total control sobre las sendas, sobre ','todo la de sombra, posee a su servicio a los mastines de sombra, los','cuales al morder a su enemigo lo infectan con la oscuridad. ','Tambien puede envenenar a sus enemigos con magia']
    
    def inmovilizar(self,jugador,oponente):
        oponente.envenenado=True
    
    def liberar_mastines_de_sombra(self,oponente):
        print('Ammanas ha liberado a los mastines de sombra')
        oponente.life-=abs(int(1.25*self.n_attack)-oponente.heal)
    
class demon(personaje,mortales):
    def __init__(self):
        personaje.__init__(self,1)
        mortales.__init__(self)
        self.name='Anomander Rake, Son of Darkness, Lord of the High House of Death'
        self.n_attack=3
        self.heal=3
        self.envenenado=False
        self.movimientos={'Atacar':'    Daño: 3', 'Desenvainar Dragnipur':'Utiliza tu espada para tomar el alma de tu oponente\n    +20% de daño', 'Soletaken':'Conviertete a tu forma de Dragón\n    +20% de Curación\n    +23% de Daño', 'Curacion con senda':'Accede a tu senda para curarte\n    Se recomienda escoger la Senda Kurald Galain'}
        self.espada_desenvainada=False
        self.descripcion=['Tambien conocido como Señor de la Gran Casa de Muerte, es un elfo de la','clase Tiiste Andii, posee una espada tomadora de almas conocida como ','Dragnipur. Es un cambia formas que puede convertirse en Dragón mediante','la invocación de su senda','']
    
    def desenvainar_Dragnipur(self,oponente):
        print('Dragnipur, la tomadora de almas ha sido desenvainada')
        sleep(1)
        oponente.life-=abs(int(self.n_attack*1.25)-oponente.heal)

    def convertise_soletaken(self,oponente):
        self.heal=int(self.heal*1.2)
        print('Anomander Rake se ha convertido en Soletaken (Dragón)\n +20% de curación')    
        sleep(1.5)
        self.n_attack=int(self.n_attack*1.25)
        oponente.life-=abs(int(self.n_attack)-oponente.heal)
        with open('soletaken.txt') as f:
            self.ascii = f.read().splitlines()

class skeleton(personaje):
    def __init__(self):
        super().__init__(2)
        self.name='Onos T\'Oolan, the Stonesword'
        self.n_attack=4
        self.heal=2
        self.envenenado=False
        self.movimientos={'Atacar':'    Daño: 4', 'Convertirse en Polvo':'Conviertete en polvo solo para atacar por detrás a tu enemigo\n    no es ético pero hey, estas muerto, lo ético no importa\n    +5% de Vida\n    +10% de Ataque', 'Hablar con los dioses':'Pide a los dioses que bendigan tu espada, gracias a lo cual ésta se prenderá fuego\n  +15% de Ataque'}
        self.descripcion=['Es un no muerto perteneciente a la raza de los t\'lan imass, tiene 10000','años de vida y tiene como poderes el convertirse en arena cuando se ve ','amenazado para despues resurgir detras de su enemigo y atacarlo por la','espalda. Si habla con sus dioses posee la capacidad de prender fuego a ','su espada']
    
    def convertirse_en_polvo(self,oponente):
        print('Onos t\'Oolan se ha convertido en Polvo\n+5% de vida\n+10% de ataque')
        self.life=int(1.05*self.life)
        if self.life>25:
            self.life=25
        oponente.life-=abs(int(self.n_attack*1.1)-oponente.heal)
        sleep(1)

    
    def hablar_con_los_dioses(self,oponente):
        print('Los dioses han escuchado tus palabras, te otorgan una espada de fuego\n+15% de ataque')
        self.n_attack=int(self.n_attack*1.15)
        oponente.life-=abs((self.n_attack)-oponente.heal)
        sleep(1)
