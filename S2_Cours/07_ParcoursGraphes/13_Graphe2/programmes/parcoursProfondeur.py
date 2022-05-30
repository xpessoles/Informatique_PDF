from collections import deque

def parcoursProfondeur1(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p.append(r)
            while p: # Vrai tant que p est non-vide
                s = p[-1] # sommet de la pile
                parcouru[s] = True
                sPossedeVoisin = False
                for ss in G[s]: # G[s] liste des successeurs de s dans G
                    if not parcouru[ss]:
                        sPossedeVoisin = True
                        p.append(ss)
                        break # on ne cherche qu'un voisin dans ce parcours
                if not sPossedeVoisin:
                    p.pop() # on désempile s de p qui n'a pas de voisin

def parcoursProfondeur1p(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    print(p)
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p.append(r)
            print(p)
            while p: # Vrai tant que p est non-vide
                s = p[-1] # sommet de la pile
                parcouru[s] = True
                sPossedeVoisin = False
                for ss in G[s]: # G[s] liste des successeurs de s dans G
                    if not parcouru[ss]:
                        sPossedeVoisin = True
                        p.append(ss)
                        break # on ne cherche qu'un voisin dans ce parcours
                if not sPossedeVoisin:
                    p.pop() # on désempile s de p qui n'a pas de voisin
                print(p)

G = {   'A': ['C', 'B'], 'B': ['A', 'E'], 'C': ['D', 'B'], 'D': ['C', 'E'],
        'E': [], 'F': ['A', 'C', 'D']}

# parcoursProfondeur(G)

# from pyvis.network import Network
# import networkx as nx
# Gvis = Network(height='600px', width='800px', directed=True)
# Gnx = nx.from_dict_of_lists(G, create_using=nx.MultiDiGraph)
# Gvis.from_nx(Gnx)
# Gvis.show("verif.html")

def parcoursProfondeur2p(G):
    etat = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        etat[s] = "non-découvert"
    p = deque()     # initialisation d'une deque vide
    print(p)
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if etat[r] != "exploré":
            p.append(r)
            etat[r] = "découvert"
            print(p)
            while p: # Vrai tant que p est non-vide
                s = p[-1] # sommet de la pile
                if etat[s] != "exploré":
                    for ss in G[s]: # G[s] liste des successeurs de s dans G
                        if etat[ss] == "non-découvert":
                            p.append(ss)
                            etat[ss] = "découvert"
                    etat[s] = "exploré"
                else:
                    p.pop()
                print(p)

# https://www.geeksforgeeks.org/iterative-depth-first-traversal/
def parcoursProfondeur2ip(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    print(p)
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p.append(r)
            print(p)
            while p: # Vrai tant que p est non-vide
                s = p.pop() # sommet de la pile
                if not parcouru[s]:
                    parcouru[s] = True
                for ss in G[s]: # G[s] liste des successeurs de s dans G
                    if not parcouru[ss]:
                        p.append(ss)
                print(p)

# Page 93, Algorithm Design, Kleinberg and Tardos
# cité par https://en.wikipedia.org/wiki/Depth-first_search#cite_ref-6
def parcoursProfondeur3ip(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    print(p)
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p.append(r)
            print(p)
            while p: # Vrai tant que p est non-vide
                s = p.pop() # sommet de la pile
                if not parcouru[s]:
                    parcouru[s] = True
                    for ss in G[s]: # G[s] liste des successeurs de s dans G
                        p.append(ss)
                print(p)


print("Version itérative")
parcoursProfondeur2ip(G)
parcoursProfondeur3ip(G)

def parcoursProfondeur1rp(G):
    def DFS(s):
        print(s)
        parcouru[s] = True
        for ss in G[s]:
            if not parcouru[ss]:
                DFS(ss)
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            DFS(r)

def parcoursProfondeur2rp(G):
    def DFS():
        print(p)
        s = p[-1]
        parcouru[s] = True
        for ss in G[s]:
            if not parcouru[ss]:
                p.append(ss)
                DFS()
        p.pop()
        print(p)
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    print(p)
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p.append(r)
            DFS()

print("Version récursive")
parcoursProfondeur1rp(G)
parcoursProfondeur2rp(G)
