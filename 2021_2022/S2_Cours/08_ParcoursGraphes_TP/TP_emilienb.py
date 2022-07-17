# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

## déclaration graphe sous forme d'un dictionnaire d'adjacence

# Gcav = {
#     (0, 0): [(1, 2), (2, 1)],
#     (0, 1): [(1, 3), (2, 0), (2, 2)],
#     (0, 2): [(1, 0), (1, 4), (2, 1), (2, 3)],
#     (0, 3): [(1, 1), (1, 5), (2, 2), (2, 4)],
#     (0, 4): [(1, 2), (1, 6), (2, 3), (2, 5)],
#     (0, 5): [(1, 3), (1, 7), (2, 4), (2, 6)],
#     (0, 6): [(1, 4), (2, 5), (2, 7)],
#     (0, 7): [(1, 5), (2, 6)],
#     (1, 0): [(0, 2), (2, 2), (3, 1)],
#     (1, 1): [(0, 3), (2, 3), (3, 0), (3, 2)],
#     (1, 2): [(0, 0), (0, 4), (2, 0), (2, 4), (3, 1), (3, 3)],
#     (1, 3): [(0, 1), (0, 5), (2, 1), (2, 5), (3, 2), (3, 4)],
#     (1, 4): [(0, 2), (0, 6), (2, 2), (2, 6), (3, 3), (3, 5)],
#     (1, 5): [(0, 3), (0, 7), (2, 3), (2, 7), (3, 4), (3, 6)],
#     (1, 6): [(0, 4), (2, 4), (3, 5), (3, 7)],
#     (1, 7): [(0, 5), (2, 5), (3, 6)],
#     (2, 0): [(0, 1), (1, 2), (3, 2), (4, 1)],
#     (2, 1): [(0, 0), (0, 2), (1, 3), (3, 3), (4, 0), (4, 2)],
#     (2, 2): [(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)],
#     (2, 3): [(0, 2), (0, 4), (1, 1), (1, 5), (3, 1), (3, 5), (4, 2), (4, 4)],
#     (2, 4): [(0, 3), (0, 5), (1, 2), (1, 6), (3, 2), (3, 6), (4, 3), (4, 5)],
#     (2, 5): [(0, 4), (0, 6), (1, 3), (1, 7), (3, 3), (3, 7), (4, 4), (4, 6)],
#     (2, 6): [(0, 5), (0, 7), (1, 4), (3, 4), (4, 5), (4, 7)],
#     (2, 7): [(0, 6), (1, 5), (3, 5), (4, 6)],
#     (3, 0): [(1, 1), (2, 2), (4, 2), (5, 1)],
#     (3, 1): [(1, 0), (1, 2), (2, 3), (4, 3), (5, 0), (5, 2)],
#     (3, 2): [(1, 1), (1, 3), (2, 0), (2, 4), (4, 0), (4, 4), (5, 1), (5, 3)],
#     (3, 3): [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)],
#     (3, 4): [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)],
#     (3, 5): [(1, 4), (1, 6), (2, 3), (2, 7), (4, 3), (4, 7), (5, 4), (5, 6)],
#     (3, 6): [(1, 5), (1, 7), (2, 4), (4, 4), (5, 5), (5, 7)],
#     (3, 7): [(1, 6), (2, 5), (4, 5), (5, 6)],
#     (4, 0): [(2, 1), (3, 2), (5, 2), (6, 1)],
#     (4, 1): [(2, 0), (2, 2), (3, 3), (5, 3), (6, 0), (6, 2)],
#     (4, 2): [(2, 1), (2, 3), (3, 0), (3, 4), (5, 0), (5, 4), (6, 1), (6, 3)],
#     (4, 3): [(2, 2), (2, 4), (3, 1), (3, 5), (5, 1), (5, 5), (6, 2), (6, 4)],
#     (4, 4): [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)],
#     (4, 5): [(2, 4), (2, 6), (3, 3), (3, 7), (5, 3), (5, 7), (6, 4), (6, 6)],
#     (4, 6): [(2, 5), (2, 7), (3, 4), (5, 4), (6, 5), (6, 7)],
#     (4, 7): [(2, 6), (3, 5), (5, 5), (6, 6)],
#     (5, 0): [(3, 1), (4, 2), (6, 2), (7, 1)],
#     (5, 1): [(3, 0), (3, 2), (4, 3), (6, 3), (7, 0), (7, 2)],
#     (5, 2): [(3, 1), (3, 3), (4, 0), (4, 4), (6, 0), (6, 4), (7, 1), (7, 3)],
#     (5, 3): [(3, 2), (3, 4), (4, 1), (4, 5), (6, 1), (6, 5), (7, 2), (7, 4)],
#     (5, 4): [(3, 3), (3, 5), (4, 2), (4, 6), (6, 2), (6, 6), (7, 3), (7, 5)],
#     (5, 5): [(3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6)],
#     (5, 6): [(3, 5), (3, 7), (4, 4), (6, 4), (7, 5), (7, 7)],
#     (5, 7): [(3, 6), (4, 5), (6, 5), (7, 6)],
#     (6, 0): [(4, 1), (5, 2), (7, 2)],
#     (6, 1): [(4, 0), (4, 2), (5, 3), (7, 3)],
#     (6, 2): [(4, 1), (4, 3), (5, 0), (5, 4), (7, 0), (7, 4)],
#     (6, 3): [(4, 2), (4, 4), (5, 1), (5, 5), (7, 1), (7, 5)],
#     (6, 4): [(4, 3), (4, 5), (5, 2), (5, 6), (7, 2), (7, 6)],
#     (6, 5): [(4, 4), (4, 6), (5, 3), (5, 7), (7, 3), (7, 7)],
#     (6, 6): [(4, 5), (4, 7), (5, 4), (7, 4)],
#     (6, 7): [(4, 6), (5, 5), (7, 5)],
#     (7, 0): [(5, 1), (6, 2)],
#     (7, 1): [(5, 0), (5, 2), (6, 3)],
#     (7, 2): [(5, 1), (5, 3), (6, 0), (6, 4)],
#     (7, 3): [(5, 2), (5, 4), (6, 1), (6, 5)],
#     (7, 4): [(5, 3), (5, 5), (6, 2), (6, 6)],
#     (7, 5): [(5, 4), (5, 6), (6, 3), (6, 7)],
#     (7, 6): [(5, 5), (5, 7), (6, 4)],
#     (7, 7): [(5, 6), (6, 5)]}

## déclaration des fonctions

def parcoursProfondeur(G):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                explorationProfondeur(ss) # appel récursif
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(r)

def parcoursLargeur(G):
    def explorationLargeur(r):
        f = deque() # initialisation d'une deque vide
        f.append(r)
        parcouru[r] = True
        while f:    # Vrai tant que f est non-vide
            s = f.popleft()
            for ss in G[s]: # G[s] liste des successeurs de s dans G
                if not parcouru[ss]:
                    f.append(ss)
                    parcouru[ss] = True
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(r)

def estDansEch(i, j):
    return 0 <= i < 8 and 0 <= j < 8

def mvtsPossibles(i, j):
    L = []
    for ai in [1, 2]:
        aj = 3 - ai
        for ei in [-1, 1]:
            for ej in [-1, 1]:
                di = ei*ai
                dj = ej*aj
                if estDansEch(i+di, j+dj):
                    L.append((i+di, j+dj))
    return L


def largeur_dep(G, dep):
    def explorationLargeur(r):
        f = deque() # initialisation d'une deque vide
        f.append(r)
        parcouru[r] = True
        while f:    # Vrai tant que f est non-vide
            s = f.popleft()
            for ss in G[s]: # G[s] liste des successeurs de s dans G
                if not parcouru[ss]:
                    f.append(ss)
                    parcouru[ss] = True
                    distance[ss] = distance[s] + 1
    parcouru = {}   # dictionnaire de booléens pour le marquage
    distance = {}
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
        distance[s] = -1 # initialisation des distances
    distance[dep] = 0
    explorationLargeur(dep)
    return distance


## programme principal
#Q4
def make_graphe():
    G = {}
    for i in range(8):
        for j in range(8):
            G[(i, j)] = mvtsPossibles(i, j)
    return G

G=make_graphe()
d = largeur_dep(G, (4, 3))
# d = largeur_dep(G, (0, 0))

for j in range(7, -1, -1):
    for i in range(8):
        print(d[(i, j)], end = '\t')
    print()


##### Chevre/loup

# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

## déclaration graphe sous forme d'un dictionnaire d'adjacence

G = {
    'PLCX': ['LX'], 'PCX': ['X', 'C'], 'PLX': ['LX', 'X', 'L'],
    'LX': ['PLCX', 'PLX'], 'X': ['PCX', 'PLX'], 'PLC': ['C', 'L'],
    'PC': ['C', ''], 'C': ['PCX', 'PLC', 'PC'], 'L': ['PLX', 'PLC'], '': ['PC']}

## déclaration des fonctions

def parcoursProfondeur(G):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                explorationProfondeur(ss) # appel récursif
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(r)

def parcoursLargeur(G):
    def explorationLargeur(r):
        f = deque() # initialisation d'une deque vide
        f.append(r)
        parcouru[r] = True
        while f:    # Vrai tant que f est non-vide
            s = f.popleft()
            for ss in G[s]: # G[s] liste des successeurs de s dans G
                if not parcouru[ss]:
                    f.append(ss)
                    parcouru[ss] = True
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(r)

def existence_chemin(G, dep, arr):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if ss == arr:
                return True
            if not parcouru[ss]:
                res = explorationProfondeur(ss) # appel récursif
                if res == True:
                    return True
        return False
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    if dep == arr:
        return True
    res = explorationProfondeur(dep)
    return res

def trouver_chemin(G, dep, arr):
    def explorationProfondeur(s):
        parcouru[s] = True
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if ss == arr:
                predecesseur[ss] = s
                return True
            if not parcouru[ss]:
                res = explorationProfondeur(ss) # appel récursif
                predecesseur[ss] = s
                if res == True:
                    return True
        return False
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False # initialisation du marquage
    predecesseur = {}
    explorationProfondeur(dep)
    # reconstruction du chemin
    f = deque([arr])
    sommet = arr
    while sommet != dep:
        sommet = predecesseur[sommet]
        f.appendleft(sommet)
    return list(f)



## programme principal
parcoursProfondeur(G)
parcoursLargeur(G)

print(existence_chemin(G, 'PLCX', ''))
print(trouver_chemin(G, 'PLCX', ''))
