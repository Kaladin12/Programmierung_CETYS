from personajes import *

mipersonaje=mage()
barras_disp=10
vida_rest=int(150/25)
print(vida_rest)
print('|', end='')
for i in range(vida_rest):
    print('-',end='')
if vida_rest<10:
    for i in range(10-vida_rest):
        print(' ',end='')
print('|')