numeros=[1,2,3,4,5]
num=[]
dividir=map(lambda substr: substr.capitalize() ,input('agrega: '))
for i in dividir:
    print(i)
lista=map(lambda x,y: x*y, numeros,numeros)
for i in lista:
    print(i)

def mayusculas(letra):
    return str(letra).upper()

a=list(map(str, input('dd')))
print(a)