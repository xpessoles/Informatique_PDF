# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:21:12 2023

@author: xpess
"""

## TRI SELECTION
def recherche_minimum(L : list, i : int) -> int :
    # Attention à ne pas utiliser i dans la boucle for...
    mini = i
    for j in range(i,len(L)):
        compteur()
        if L[j] < L[mini] :
            mini = j
    return mini

def inversion(L : list, i : int, j : int) -> None :
    L[i],L[j] = L[j],L[i]

def tri_selection(L : list) -> None :
    for i in range(len(L)):
        m = recherche_minimum(L,i)
        inversion(L,i,m)

## TRI RAPIDE
def elts_inf(L : list, p : int) -> list :
    res = []
    for e in L :
        compteur()
        if e<p :
            res.append(e)
    return res

def elts_sup(L : list, p : int) -> list :
    res = []
    for e in L :
        compteur()
        if e>=p :
            res.append(e)
    return res

def tri_rapide(L : list) -> list :
    if len(L) == 0 :
        return []
    else : 
        p = L[-1]
        ei = elts_inf(L,p)
        es = elts_sup(L[:-1],p)
        return tri_rapide(ei) + [p] + tri_rapide(es)
    

## TRI FUSION
def separe(L: list) -> tuple[list,list]:
    return L[:len(L) // 2], L[len(L) // 2:]

def fusion(L1: list, L2: list) -> list:
    compteur()
    if not L1 or not L2: # si l'une des listes est vide (éventuellement les 2)
        return L1 or L2 # alors on renvoie l'autre (éventuellement vide aussi)
    else:
        a, b = L1[0], L2[0] 
        if a < b : # sinon on compare leurs premiers éléments
            return [a] + fusion(L1[1:], L2) # on place le plus petit en tête et on fusionne le reste
        else:
            return [b] + fusion(L1, L2[1:])
        

def tri_fusion(L: list) -> list:
    if len(L) < 2: # cas d'arrêt
        return L
    L1, L2 = separe(L) # sinon on sépare
    return fusion(tri_fusion(L1), tri_fusion(L2)) # et on fusionne les sous-listes triées

## TRI COMPTAGE
def tri_comptage(L:list):
    k = max(L)
    C=k*[0]
    a=[]
    for x in L:
        for i in range(k):
            compteur()
            if x==i:
                C[i]+=1
    for i in range(k):
        a+=C[i]*[i]
    return a


## Compteur

C = 0
def compteur():
    global C
    C = C+1	
    
"""
C=0
tri_fusion([3,2,1,1,0,1,2,3,0,4,3,2,1])
print("Fusion", C)

C=0
tri_comptage([3,2,1,1,0,1,2,3,0,4,3,2,1])
print("Comptage", C)

C=0
tri_selection([3,2,1,1,0,1,2,3,0,4,3,2,1])
print("Selection", C)

C=0
tri_rapide([3,2,1,1,0,1,2,3,0,4,3,2,1])
print("Rapide", C)
"""
import matplotlib.pyplot as plt
import random as rd
    
les_i = []
les_selection = []
les_comptage = []
les_rapide = []
les_fusion = []
for i in range(1,200,10):
    #print(i)
    les_i.append(i)
    
    L = [rd.randrange(0,i) for x in range(i)]
    
    
    C = 0
    tri_selection(L.copy())
    les_selection.append(C)
    
    C = 0
    tri_comptage(L.copy())
    les_comptage.append(C)
    
    C = 0
    tri_rapide(L.copy())
    les_rapide.append(C)
    
    C = 0
    tri_fusion(L.copy())
    les_fusion.append(C)
    
plt.plot(les_i,les_selection,label='Selection')
plt.plot(les_i,les_comptage,label='Comptage')
plt.plot(les_i,les_rapide,label='Rapide')
plt.plot(les_i,les_fusion,label='Fusion')
import math as m
les_ln = [i*m.log(i) for i in les_i]
plt.plot(les_i,les_ln,label='n*ln(n)')

les_carres = [i*i for i in les_i]
plt.plot(les_i,les_carres,label='Carres')


plt.grid()
plt.legend()
plt.show()





# ###
    
# les_i = []
# les_selection = []
# les_comptage = []
# les_rapide = []
# les_fusion = []
# for i in range(1,10000,500):
#     print(i)
#     les_i.append(i)
    
#     L = [rd.randrange(0,i) for x in range(i)]
    
#     C = 0
#     tri_rapide(L.copy())
#     les_rapide.append(C)
    
#     C = 0
#     tri_fusion(L.copy())
#     les_fusion.append(C)
    

# plt.plot(les_i,les_rapide,label='Rapide')
# plt.plot(les_i,les_fusion,label='Fusion')
# import math as m
# les_ln = [i*m.log(i) for i in les_i]
# plt.plot(les_i,les_ln,label='Ln')
# plt.grid()
# plt.legend()
# plt.show()
