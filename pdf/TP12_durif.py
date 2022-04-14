#Q1
print('Q1 : ')
print(1.0 + (2**53 - 2**53))
print((1.0 + 2**53) - 2**53)
print((1 + 2**53) - 2**53)


#Q2
print((0.1+0.2) - 0.3 == 0)

#Q3
print(1/1000-1/1001)
print(1/(1000*1001))


#Q4-5
mc=0.5
i=0
while 1+mc!=1:
    mc=mc/2
    i+=1

#Q6
import math as m
print(m.sqrt(2).hex())
print(1+6/16+10/16**2+9/16**4++14/16**5+6/16**6+6/16**7,m.sqrt(2))


#Q7
def f(u:int)->int:
    return (16805*u+1)%2**15
u=13
for k in range(1000):
    u=f(u)
    print(u)

#Q8
def binaire(e:int)->str:
    s=''
    while e>0:
        s=str(e%2)+s
        e=e//2
    return s

#Q9
def booleen(e:int,n:int)->str:
    s=binaire(e)
    s=(n-len(s))*'0'+s
    return s[-n]


#Q10
u=13
L=[]
for k in range(10000):
    u=f(u)
    if booleen(u,1)=='1':
        L.append(u)

#Q11
u=13
L11=[]
for k in range(10000):
    u=f(u)
    if booleen(u,9)=='1':
        L11.append(u)


#Q12
u=13
u=f(u)
k=1
while u!=13:
    u=f(u)
    k+=1
#La periode apparente de la suite est 32768

#Q13
u=13
L=[]
for k in range(32768):
    u=f(u)
    if booleen(u,1)=='1':
        L.append(u)

L_c=32768*[0]
for x in L:
    L_c[x]+=1



#On vérifier bien que max(L_c)=1
L13=[]
i=0
for x in L_c:
    if x==1:
        L13.append(i)
    i+=1

#On a  len(L13)=32768/2

#Q14
from random import randint
L14=[]
for k in range(100000):
    L14.append(randint(0,100000))


#Q15
import time


