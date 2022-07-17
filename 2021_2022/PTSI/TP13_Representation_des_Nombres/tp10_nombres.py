### TP10 representation des nombres
import numpy as np
import random as r
import time as t


# absorption
# >>> 1.0+(2**53-2**53)
# 1.0
# >>> (1.0+2**53)-2**53
# 0.0
# >>> (1+2**53)-2**53
# 1
# la petite quantité 1 a été absorbée par la grande sauf dans le dernier cas qui traite des entiers

# des erreurs d'arrondis
# >>> (0.1+0.2)-0.3==0
# False
# 0.1 ne s'exprime pas de façon finie avec des 1/2**k
#  il a un nombre infini de chiffres binaires après la virgule

# phénomène de cancellation
# >>> 1/1000-1/1001
# 9.990009990010207e-07
# >>> 1/(1000*1001)
# 9.99000999000999e-07
# il vaut mieux calculer 1/(x*(x+1)) plutôt que 1/x-1/(x+1)



def mantisse(x):
    i=0
    while not x+1==1:
        x=x/2
        i=i+1
    return i

# >>> mantisse(0.5)
# 52

# >>> a=np.sqrt(2)
# >>> a.hex()
# '0x1.6a09e667f3bcdp+0'
# bit de signe 0, mantisse (6a09e667f3bcd)16 et exposant 0
# mantisse en binaire
# 0110 1010 0000 1001 1110 0110 0110 0111 1111 0011 1011 1100 1101

### générateur de nombres aléatoires
def f(u):
    return (16805*u+1)%2**15


u=[13]
for i in range(1000):
    un=f(u[-1])
    u.append(un)
# print (u)

# [13, 21858, 27179, 22712, 26265, 31134, 215, 8596, 14437, 32282, 24771, 24752, 3
# 69, 7894, 13807, 29196, 3517, 22482, 27739, 29096, 26953, 25870, 12295, 15236, 2
# 4597, 17034, 27891, 27552, 32289, 11334, 20255, 24060, 3949, 7746, 17035, 11928,

# >>> (executing file "tp10_nombres.py")
# [13, 21858, 27179, 22712, 26265, 31134, 215, 8596, 14437, 32282, 24771, 24752, 3
# 69, 7894, 13807, 29196, 3517, 22482, 27739, 29096, 26953, 25870, 12295, 15236, 2
# 4597, 17034, 27891, 27552, 32289, 11334, 20255, 24060, 3949, 7746, 17035, 11928,

# les nombres paraissent aléatoires mais sont toujours les mêmes

### génération de booléens
def binaire(e:int):
    b=''
    while not e//2==0:
        b=str(e%2)+b
        e=e//2
    b=str(e%2)+b
    return b

# >>> binaire(5)
# '101'
# >>> binaire(94)
# '1011110'
# >>> bin(94)
# '0b1011110'

def booleen(e:int,n:int):
    b=binaire(e)
    m=len(b)
    if m<n:
        rep='0'
    else:
        rep=b[m-n]
    return rep

# bit de poids faible
s=0
u=13
liste_u=[]
for i in range(10000):
    h=booleen(u,1)
    s=s+int(h)
    u=f(u)
    if i<100:
        liste_u.append(h)


# >>> s
# 5000
# >>> liste_u
# ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'

s9=0
u=13
liste_u9=[]
for i in range(10000):
    h9=booleen(u,9)
    s9=s9+int(h9)
    u=f(u)
    if i<100:
        liste_u9.append(h9)


# >>> liste_u9
# ['0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0']
#
# >>> s9
# 5008

### génération d'un entier quelconque
i=1
u=13
u=f(u)
while not u==13:
    i+=1
    u=f(u)
# print (i)

# >>> (executing file "tp10_nombres.py")
# 32768

L=[0]*32768
u=13
for i in range(32770):
    L[u]+=1
    if L[u]>1:
        print (str(u)+' apparait '+str(L[u])+' fois')
    u=f(u)
if max(L)==1:
    print ('Tous les nombres apparaissent une seule fois')

# >>> (executing file "tp10_nombres.py")
# Tous les nombres apparaissent une seule fois
# >>> (executing file "tp10_nombres.py")
# 13 apparait 2 fois
# 21858 apparait 2 fois

# test randint
L=[0]*32769
for i in range(100000):
    u=r.randint(0,32768)
    L[u]+=1
    # if L[u]>1:
    #     print (str(u)+' apparait '+str(L[u])+' fois')

# >>> L
# [2, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 1, 0, 1, 2, 1, 1, 1, 1, 0, 3, 0, 1, 0, 0, 0, 0
# , 4, 0, 1, 2, 1, 1, 1, 0, 2, 4, 2, 2, 2, 1, 0, 0, 0, 0, 1, 1, 0, 2, 2, 2, 0, 2,
# 2, 4, 2, 1, 2, 2, 0, 3, 0, 2, 1, 0, 2, 2, 2, 3, 0, 1, 1, 2, 0, 5, 1, 2, 0, 1, 2,
#  0, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0, 1, 0, 0, 3, 1, 4, 0, 2, 1, 1
# , 1, 0, 3, 0, 3, 1, 3, 1, 0, 2, 2, 1, 1, 2, 2, 2, 0, 0, 0, 0, 1, 1, 0, 2, 2, 2,
# 2, 1, 0, 0, 2, 3, 1, 1, 1, 0, 3, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 2, 0,
#  2, 1, 1, 3, 3, 0, 0, 4, 1, 1, 1, 1, 2, 1, 0, 2, 1, 2, 2, 1, 0, 1, 0, 0, 2, 3, 2


# >>> L[:100]
# [1, 2, 4, 1, 6, 3, 7, 2, 1, 3, 3, 1, 4, 3, 2, 4, 5, 3, 4, 1, 3, 4, 3, 2, 5, 3, 4, 0, 2, 4, 2, 4, 3, 2, 2, 2, 5, 3, 2, 2, 8, 1, 1, 5, 3, 1, 3, 3, 7, 6, 6, 5, 4, 3, 4, 1, 2, 3, 3, 6, 5, 1, 2, 4, 4, 3, 2, 8, 0, 4, 4, 1, 2, 5, 1, 2, 4, 1, 2, 7, 3, 2, 3, 2, 4, 3, 2, 5, 5, 5, 1, 1, 3, 1, 6, 3, 7, 3, 4, 3]

# question 15
# >>> t.perf_counter()
# 84781.4376918


def graine():
    x=int(t.perf_counter()*10**7)
    x=x%(2**15-1)
    return x

# >>> graine()
# 23090

def aleatoire(n:int):
    u=graine()
    L=[]
    for i in range(n):
        pile=booleen(u,9)
        L.append(int(pile))
        u=f(u)
    return L

# >>> aleatoire(10)
# [0, 0, 1, 0, 0, 0, 1, 0, 0, 1]












