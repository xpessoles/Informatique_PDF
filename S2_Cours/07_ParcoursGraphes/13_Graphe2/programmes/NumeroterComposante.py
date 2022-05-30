from collections import deque

def explorationLargeur(G, r, parcouru, composante, i):
    f = deque() # initialisation d'une deque vide
    f.append(r)
    parcouru[r] = True
    composante[r] = i
    while f:    # Vrai tant que f est non-vide
        s = f.popleft()
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                f.append(ss)
                parcouru[ss] = True
                composante[ss] = i

def parcoursLargeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    composante = {} # dictionnaire d'entiers pour les composantes
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    num_comp = 0 # compteur de composantes
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationLargeur(G, r, parcouru, composante, num_comp)
            num_comp += 1 # incrémentation du compteur de composante
    return composante

G = {   'A': ['B', 'C'], 'B': ['A', 'C', 'E'], 'C': ['E', 'G'],
        'D': ['C', 'E', 'F'], 'E': [], 'F': ['C'], 'G': ['A']}

res = parcoursLargeur(G)

print(res)