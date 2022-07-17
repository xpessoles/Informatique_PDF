# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:06:41 2021

@author: xpess,
Serge BAYS https://mathematice.fr/
"""

objets = [['objet 1', 126, 14], ['objet 2', 32, 2],['objet 3', 20, 5], ['objet 4', 5, 1],
['objet 5', 18, 6], ['objet 6', 80, 8]]


def valeur(obj):
    return obj[1]
def poids(obj):
    return 1 / obj[2]
def rapport(obj):
    return obj[1] / obj[2]

def glouton(liste, poids_max, choix):
    copie = sorted(liste, key=choix, reverse=True)
    reponse = []
    valeur = 0
    poids = 0
    i = 0
    while i < len(liste) and poids <= poids_max:
        nom, val, pds = copie[i]
        if poids + pds <= poids_max:
            reponse.append(nom)
            poids = poids + pds
            valeur = valeur + val
        i = i + 1
    return reponse, valeur


## ALGO RECURSIF
def solution(liste, poids_max, choix):
    copie = sorted(liste, key=choix, reverse=True)
    return glouton_rec(copie, poids_max, [], 0, 0, 0)

def glouton_rec(liste, poids_max, reponse, valeur, poids, i):
    if i < len(liste) and poids <= poids_max:
        nom, val, pds = liste[i]
        if poids + pds <= poids_max:
            reponse.append(nom)
            poids = poids + pds
            valeur = valeur + val
        return glouton(liste, poids_max, reponse, valeur, poids, i+1)
    else:
        return reponse, valeur