##### TP 5

##### Recherche dans une liste triée.

## I.1

## Q1

# g=0, d=8
# m=4, L[m]=11 et 5 < 11, on pose g=0, d=3
# m=2, L[m]=5. On a trouvé x0

# g=0, d=8
# m=4, L[m]=8 et 8<11, on pose g=5, d=8
# m=6, L[m]=13 et 11<13, on pose g=5, d=5
# m=5, L[m]=10 et 10<11, on pose g=6, d=5. On s'arrête.


## Q2

def dichotomie(x0,L):
    Test=False
    n=len(L)
    g,d=0,n-1
    while g<=d and not Test:
        m=(g+d)//2
        if L[m]==x0:
            Test=True
        elif L[m]>x0:
            d=m-1
        else:
            g=m+1
    return(Test)

## Q3

# Si x0 n_est pas présent, on exécute la boucle tant que g<=d. On sort avec g=d+1.
# A l_entrée du 1er tout de boucle, on a d-g+1=n. A chaque tour, la valeur d-g+1 diminue environ de moitié. Donc après k tours de boucles, la longueur de l_intervalle est de l_ordre de n/2**k.
# De plus, à chaque tour de boucle, il y a 2 comparaisons.
# Au dernier tour numéro k, on a g=d soit lorsque n/2**k = 1 d_ou k=log_2(n).
# On obtient donc un nombre de comparaisons équivalent à 2*ln(n)/ln(2): complexité logarithmique.
# Dans le cas séquentiel, on obtient une complexité linéaire, donc beaucoup moins intéressant.

## I.2

# L'idée est de s'arrêter lorsque d-g=1 avec L[g]\>0>L[d]

def recherche_dicho(L):
    n=len(L)
    g,d=0,n-1
    while d-g>1:
        m=(g+d)//2
        if L[m]>=0:
            g=m
        else:
            d=m
    return(g,L[g])

## I.3

## 1

# Pour une valeur à epsilon près, on s_arrete lorsque 0<d-g<2*epsilon et on renvoie (g+d)/2

## 2

def recherche_zero(f,a,b,epsilon):
    g,d=a,b
    while d-g>2*epsilon:
        m=(g+d)/2
        if f(m)*f(g)<=0:
            d=m
        else:
            g=m
    return((g+d)/2)


## 3

def f(x):
    return(x**2-2)

# print(recherche_zero(f,0,2,0.001)

## 4

# Avec epsilon = 1/2**p, il faut compter combien il y a de tours de boucles. En sortie du kieme tour de boucle, d-g vaut (b-a)/2**k. Il y a donc k tours de boucles avec (b-a)/2**k<=1/2**(p-1) soit k>=p-1+log_2(b-a) soit une complexité logarithmique encore.



##### II. Exponentiation rapide.

import numpy as np
import matplotlib.pyplot as plt
import time as t
import random as r

## 1.(a)

def exponaif(x,n):
    p=1
    for i in range(n):
        p=p*x
    return(p)

# Le nombre d'opérations effectuées est exactement n (1 produit à chaque tour)


## 1.(b)

def exporapide(x,n):
    y=x
    k=n
    p=1
    while k>0:
        if k % 2==1:
            p=p*y
        y=y*y
        k=k//2
    return(p)

# A chaque tour de boucle, il y a au plus 1 comparaison et 2 ou 3 opérations. En sortie du ième tour, k vaut environ n/2**k. On sort de la fonction lorsque n/2**k vaut 1 soit k=ln(n)/ln(2).
# Le nombre d_opérations est donc compris entre 2*ln(n)/ln(2) et 3*ln(n)/ln(2): complexité logarithmique en O(ln(n)).

## 2

## 2;(a)

import time as t

def Pnaif(x,n):
    S=0
    for i in range(n):
        S=S+i*exponaif(x,i)
    return(S)

# n+n(n+1)/2 ~ n**2/2 opérations. Quadratique

## 2. (b)

def Prapide(x,n):
    S=0
    for i in range(n):
        S=S+i*exporapide(x,i)
    return(S)

# O(log(i)) pour chaque i*x**i. Il reste la somme des n termes.
# D'où n+somme des log(i)=O(n.ln(n)).

## 2. (c)

def Phorner(x,L):
    """L est la liste des coefficients"""
    n=len(L)-1
    S=0
    for i in range(n+1):
        S=S*x+L[n-i]
    return(S)

# 2n opérations. Linéaire mais plus intéressante que ci-dessus.

## 3

# Liste des temps d'exécution pour le calcul de x**n pour n=0..50 :

N=[i for i in range(101)]

# Tracé des temps pour les calculs de P(x) avec n=0..100 avec P(x)=somme des iX**i, i=0..n

def Temps_calcul_P(x):
    # Le polynôme est donné par une liste des coefficients.
    Tn,Tr,Th=[],[],[]
    for n in N:
        L=[k for k in range(n+1)]
        tps=t.perf_counter()
        Pnaif(x,n)
        Tn.append(t.perf_counter()-tps)
        tps=t.perf_counter()
        Sr=0
        Prapide(x,n)
        Tr.append(t.perf_counter()-tps)
        tps=t.perf_counter()
        Phorner(x,L)
        Th.append(t.perf_counter()-tps)
    plt.plot(N,Th,label='méthode horner')
    plt.plot(N,Tr,label='méthode rapide')
    plt.plot(N,Tn,label='méthode naïve')
    plt.legend()
    plt.show()

#####



