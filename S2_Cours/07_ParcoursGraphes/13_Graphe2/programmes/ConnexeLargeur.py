from collections import deque

def connexeLargeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    f = deque()     # initialisation d'une deque vide
    connexe = {}    # dictionnaire de connexité
    numConex = 0
    for r in G:     # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            parcouru[r] = True
            f.append(r)
            while f: # Vrai tant que f est non-vide
                s = f.popleft()
                connexe[s] = numConex
                for ss in G[s]: # G[s] liste des successeurs de s dans G
                    if not parcouru[ss]:
                        parcouru[ss] = True
                        f.append(ss)
            numConex += 1
    return connexe

G = {   'A': ['B', 'C'], 'B': ['A', 'C', 'E'], 'C': ['E', 'G'],
        'D': ['C', 'E', 'F'], 'E': [], 'F': ['C'], 'G': ['A']}
print(connexeLargeur(G))

G = {   'A': ['C', 'B'], 'B': ['A', 'E'], 'C': ['D', 'B'], 'D': ['C', 'E'],
        'E': [], 'F': ['A', 'C', 'D']}
print(connexeLargeur(G))
