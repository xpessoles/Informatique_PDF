from collections import deque

def explorationLargeur(G, r, parcouru):
    f = deque() # initialisation d'une deque vide
    f.append(r)
    parcouru[r] = True
    while f:    # Vrai tant que f est non-vide
        s = f.popleft()
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                f.append(ss)
                parcouru[ss] = True

def parcoursLargeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(G, r, parcouru)

def explorationLargeur(G, r, parcouru):
    f = deque() # initialisation d'une deque vide
    print(f)
    f.append(r)
    print(f)
    parcouru[r] = True
    while f:    # Vrai tant que f est non-vide
        s = f.popleft()
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                f.append(ss)
                parcouru[ss] = True
        print(f)

def parcoursLargeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(G, r, parcouru)


G = {   'A': ['B', 'C'], 'B': ['A', 'C', 'E'], 'C': ['E', 'G'],
        'D': ['C', 'E', 'F'], 'E': [], 'F': ['C'], 'G': ['A']}

parcoursLargeur(G)

from pyvis.network import Network
import networkx as nx
Gvis = Network(height='600px', width='800px', directed=True)
Gnx = nx.from_dict_of_lists(G, create_using=nx.MultiDiGraph)
Gvis.from_nx(Gnx)
Gvis.show("verif.html")