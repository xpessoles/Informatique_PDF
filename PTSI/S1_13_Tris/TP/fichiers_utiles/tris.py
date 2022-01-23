### algorithmes de tris
###Tri par insertion :
# méthode 1 : comparaison avec le premier élément de la partie de la liste triée
def tri_Insertion(t:list) :
    '''Trie la liste t
    Entrée :
        Une liste
    Sortie :
        La liste est modifiée mais n’est pas renvoyée'''
    for i in range(1,len(t)) :
        x=t[i]
        k=0
        while (k<i and x>t[k]) :
            k=k+1
        for j in range(i,k,-1) :
            t[j]=t[j-1]
        t[k]=x


###Tri rapide ou quicksort :
# méthode 1 : création de deux listes vides "temporaires"
def tri_rapide(t) :
    '''Trie la liste t par une méthode récursive
    Entrée :
        Une liste
    Sortie :
        La liste modifiée'''
    if len(t)<2 :
        return (t)
    else :
        x=t[-1]
        a=[]
        b=[]
        for i in range(0,len(t)-1) :
            if t[i]<x :
                a.append(t[i])
            else :
                b.append(t[i])
        return (tri_rapide(a)+[x]+tri_rapide(b))

# méthode 2
def partition(tab,g,d) :
    """Partition d'un tableau par rapport à un pivot.
    Entrée :
        tab (list) -- liste de nombres
        g,d (int) -- indices de fin et de début de la segmentation
    Sortie :
        tab (list) -- liste de nombres avec le pivot à sa place définitive est modifiée mais pas renvoyée
        p (int) -- indice de la place du pivot"""
    p=d
    pivot=tab[d]
    for i in range(d-1,g-1,-1) :
        if tab[i]>pivot :
            p=p-1
            tab[p],tab[i]=tab[i],tab[p]
    tab[p],tab[d]=tab[d],tab[p]
    return p


def tri_quicksort(tab,i,j):
    """Tri d'une liste par l'utilisation du tri rapide (Quick sort).
    Entrée :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la zone de tri
    Sortie :
        tab (list) -- liste de nombres avec le pivot à sa place définitive"""
    if i<j :
        k = partition(tab,i,j)
        tri_quicksort(tab,i,k-1)
        tri_quicksort(tab,k+1,j)

###Tri par fusion :
def placer(L,p,x) :
    '''Place un élément à sa place dans une liste triée à partir de l’indice p
    Entrée :
        L : une liste
        p : un entier
        x : un élément
    Sorties :
        La liste est modifiée mais n’est pas renvoyée
        k la valeur de l’indice de la liste où l’élément a été placé'''
    k=p
    while (k<len(L) and x>L[k]) :
        k=k+1
    L.insert(k,x)
    return (k)

def fusion(a,b) :
    '''Fusionne les deux listes
    Entrée :
        deux listes a et b
    Sortie :
        La liste b modifiée'''
    p=0
    for x in a :
        p=placer(b,p,x)+1
    return (b)

def tri_fusion(t) :
    '''Trie la liste t
    Entrée :
        Une liste
    Sortie :
        La liste est modifiée'''
    if len(t)<2 :
        return (t)
    else :
        m=len(t)//2
        return (fusion(tri_fusion(t[:m]),tri_fusion(t[m:])))

import random as rd
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)




