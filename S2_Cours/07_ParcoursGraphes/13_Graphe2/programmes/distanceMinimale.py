from collections import deque

def distance(G, r):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    f = deque()     # initialisation d'une deque vide
    parcouru[r] = True
    distance = {}       # dictionnaire des distances
    predecesseur = {}   # dictionnaire des prédecesseurs
    f.append(r)
    distance[r] = 0
    while f: # Vrai tant que f est non-vide
        s = f.popleft()
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if not parcouru[ss]:
                parcouru[ss] = True
                f.append(ss)
                distance[ss] = distance[s] + 1 # incrément de la distance
                predecesseur[ss] = s # mémorisation du prédecesseur
    return distance, predecesseur

G = {   'A': ['B', 'C'], 'B': ['A', 'C', 'E'], 'C': ['E', 'G'],
        'D': ['C', 'E', 'F'], 'E': [], 'F': ['C'], 'G': ['A']}

print(distance(G, 'A'))
print(distance(G, 'D'))

