from collections import deque

def connexeProfondeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    p = deque()     # initialisation d'une deque vide
    connexe = {}    # dictionnaire de connexité
    numConex = 0
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
                    connexe[s] = numConex # on ne le fait qu'1 fois à la sortie
            numConex += 1
    return connexe

G = {   'A': ['B', 'C'], 'B': ['A', 'C', 'E'], 'C': ['E', 'G'],
        'D': ['C', 'E', 'F'], 'E': [], 'F': ['C'], 'G': ['A']}
print(connexeProfondeur(G))

G = {   'A': ['C', 'B'], 'B': ['A', 'E'], 'C': ['D', 'B'], 'D': ['C', 'E'],
        'E': [], 'F': ['A', 'C', 'D']}
print(connexeProfondeur(G))
