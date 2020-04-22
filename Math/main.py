#Sistemas de congruencias
'''text='esto es ascii'
lista=map(lambda x: x.upper(), text)
for i in lista:
    print(i, ord(i))'''

# p, q
#mcm(p-1,q-1)=A
#1<e<780
#d=invmod(e, mod A)

def inverse_mod(a,m):
    a=a%m
    for i in range(0,m):
        if ((a*i)%m==1):
            return i
    return 1

N=int(input('Cuantas congruencias? '))
a=[]
b=[]
c=[]
n=[]
for i in range(N):
    b.append(int(input('Ingresa tu b: ')))
    n.append(int(input('Ingresa tu n: ')))
M=1
for n_i in n:
    M*=n_i
for n_i in n:
    a.append(M/n_i)
for i in range(N):
    c.append(inverse_mod(a[i],n[i]))
S=0
for i in range(N):
    S+=(a[i]*b[i]*c[i])
S=S%M
print('x es congruente a ', S ,' modulo ', M) 