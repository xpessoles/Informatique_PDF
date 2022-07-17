# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:33:52 2022

@author: xavier.pessoles2
"""
import sys
sys.setrecursionlimit(100000) 
def tri_insertion(T,n):
    for i in range(1,n):
        j=i
        v=T[i]
        while j>0 and v<T[j-1]:
            T[j]=T[j-1]
            j=j-1
        T[j]=v
    return T

def partition(a,g,d):
    assert g<d
    v=a[g]
    ainf=[]
    asup=[]
    for x in a[g+1:d]:
        if x<v:
            ainf.append(x)
        else:
            asup.append(x)
    a=a[0:g]+ainf+[v]+asup+a[d:len(a)]
    m=len(ainf)+g
    return m,a

def tri_rapide(a,g,d):
    if g>=d-1:
        return
    else:
        m,a=partition(a,g,d)
        #print(a)
        tri_rapide(a,g,m)
        tri_rapide(a,m+1,d)
    
def tri_fusion(a,g,d):
    a0=a[:]
    if g>=d-1:
        return
    else:
        m=(g+d)//2
        tri_fusion(a,g,m)
        tri_fusion(a,m,d)
        a0[g:d]=a[g:d]
        fusion(a0,a,g,m,d)

def fusion(a0,a,g,m,d):
    i,j=g,m
    for k in range(g,d):
        if i<m and (j==d or a0[i]<=a0[j]):
            a[k]=a0[i]
            i=i+1
        else:
            a[k]=a0[j]
            j=j+1

import time
import matplotlib.pyplot as plt
import numpy as np
import random as rd


# Tri d'une liste triée
les_n = []
les_ti = []
les_tf = []
les_tr = []
for n in range(1,1000,10):
    L = [x for x in range(n)]
    les_n.append(n)
    # Tri insertion
    start = time.time()
    tri_insertion(L, n)
    end = time.time()
    les_ti.append(end-start)
    
    # Tri fusion
    start = time.time()
    tri_fusion(L,0,len(L))
    end = time.time()
    les_tf.append(end-start)
    
    # Tri rapide
    start = time.time()
    tri_rapide(L,0,len(L))
    end = time.time()
    les_tr.append(end-start)
    
plt.plot(les_n,les_ti,label = "Tri insertion")
plt.plot(les_n,les_tf,label = "Tri fusion")
plt.plot(les_n,les_tr,label = "Tri rapide")
plt.ylabel("Temps (s)")
plt.xlabel("Taille liste")
plt.title("Tri d'une liste triée")
plt.grid()
plt.legend()



# Tri d'une liste triée par ordre décroissant
les_n = []
les_ti = []
les_tf = []
les_tr = []
for n in range(1,1000,10):
    
    les_n.append(n)
    # Tri insertion
    L = [x for x in range(n)]
    L.reverse()
    start = time.time()
    tri_insertion(L, n)
    end = time.time()
    les_ti.append(end-start)
    
    # Tri fusion
    L = [x for x in range(n)]
    L.reverse()
    start = time.time()
    tri_fusion(L,0,len(L))
    end = time.time()
    les_tf.append(end-start)
    
    # Tri rapide
    L = [x for x in range(n)]
    L.reverse()
    start = time.time()
    tri_rapide(L,0,len(L))
    end = time.time()
    les_tr.append(end-start)
    
plt.figure()
plt.plot(les_n,les_ti,label = "Tri insertion")
plt.plot(les_n,les_tf,label = "Tri fusion")
plt.plot(les_n,les_tr,label = "Tri rapide")
plt.ylabel("Temps (s)")
plt.xlabel("Taille liste")
plt.title("Tri d'une liste triée dans l'ordre décroissant")
plt.grid()
plt.legend()


# Tri d'une liste aléatoire
les_n = []
les_ti = []
les_tf = []
les_tr = []
for n in range(1,1000,10):
    les_n.append(n)
    Ll = [rd.randrange(1,1000) for x in range(n)]
    # Tri insertion
    L = Ll.copy()
    start = time.time()
    tri_insertion(L, n)
    end = time.time()
    les_ti.append(end-start)
    
    # Tri fusion
    L = Ll.copy()
    start = time.time()
    tri_fusion(L,0,len(L))
    end = time.time()
    les_tf.append(end-start)
    
    # Tri rapide
    L = Ll.copy()
    start = time.time()
    tri_rapide(L,0,len(L))
    end = time.time()
    les_tr.append(end-start)
    
plt.figure()
plt.plot(les_n,les_ti,label = "Tri insertion")
plt.plot(les_n,les_tf,label = "Tri fusion")
plt.plot(les_n,les_tr,label = "Tri rapide")
plt.ylabel("Temps (s)")
plt.xlabel("Taille liste")
plt.title("Tri d'une liste aléatoire")
plt.grid()
plt.legend()