from collections import deque

def detectionCycle(G):
    etats = {}      # dictionnaire de chaine de caractères pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        etats[s] = 'attente'
    p = deque()     # initialisation d'une deque vide
    for r in G:     # Itération sur une clé de G
        p.append(r)
        etats[r] = 'découvert'
        break # si le graphe est connexe, pas besoin de tester plusieurs racines
    while p: # Vrai tant que p est non-vide
        s = p[-1] # sommet de la pile
        sPossedeVoisin = False
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if etats[ss] == 'attente':
                sPossedeVoisin = True
                p.append(ss)
                etats[ss] = 'découvert'
                break # on ne cherche qu'un voisin dans ce parcours
            elif etats[ss] == 'découvert' and p[-2] != ss: # /!\ cycle
                cycle = deque([ss])
                while p[-1] != ss: # tant qu'on ne retrouve pas ss
                    cycle.appendleft(p.pop()) # permet de conserver l'ordre
                cycle.appendleft(p.pop())
                return cycle
        if not sPossedeVoisin:
            p.pop() # on désempile s de p qui n'a pas de voisin
            etats[s] = 'exploré'

G = {   'a': ['b'], 'b': ['a', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'c', 'e'],
        'e': ['d']}
print(detectionCycle(G))

G = {'a': ['b'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['c']}
print(detectionCycle(G))

def detectionCycle(G):
    etats = {}      # dictionnaire de chaine de caractères pour le marquage
    for s in G:     # Itération sur les clés de G (dictionnaire de listes)
        etats[s] = 'attente'
    p = deque()     # initialisation d'une deque vide
    for r in G:     # Itération sur une clé de G
        p.append(r)
        etats[r] = 'découvert'
        break # si le graphe est connexe, pas besoin de tester plusieurs racines
    while p: # Vrai tant que p est non-vide
        s = p[-1] # sommet de la pile
        sPossedeVoisin = False
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if etats[ss] == 'attente':
                sPossedeVoisin = True
                p.append(ss)
                etats[ss] = 'découvert'
                break # on ne cherche qu'un voisin dans ce parcours
            elif etats[ss] == 'découvert' and p[-2] != ss: # /!\ cycle
                cycle = deque([ss])
                while p[-1] != ss: # tant qu'on ne retrouve pas ss
                    cycle.appendleft(p.pop()) # permet de conserver l'ordre
                cycle.appendleft(p.pop())
                return cycle
        if not sPossedeVoisin:
            p.pop() # on désempile s de p qui n'a pas de voisin
            etats[s] = 'exploré'

G = {   'a': ['b'], 'b': ['a', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'c', 'e'],
        'e': ['d']}
print(detectionCycle(G))

G = {'a': ['b'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['c']}
print(detectionCycle(G))