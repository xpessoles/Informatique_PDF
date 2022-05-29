def explorationProfondeur(G, p, parcouru):
    s = p[-1] # sommet provenant du haut de la pile
    parcouru[s] = True
    for ss in G[s]: # G[s] liste des successeurs de s dans G
        if not parcouru[ss]:
            p.append(ss) # ajout de ss dans la pile
            explorationProfondeur(G, p, parcouru) # appel récursif
    p.pop()   # haut de la pile retiré

def parcoursProfondeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p = [r]    # pile contenant uniquement la racine
            explorationProfondeur(G, p, parcouru)

def explorationProfondeur(G, p, parcouru):
    print(p)
    s = p[-1] # sommet provenant du haut de la pile
    parcouru[s] = True
    for ss in G[s]: # G[s] liste des successeurs de s dans G
        if not parcouru[ss]:
            p.append(ss)
            explorationProfondeur(G, p, parcouru)
    p.pop()   # haut de la pile retiré
    print(p)

def parcoursProfondeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            p = [r]    # pile contenant uniquement la racine
            explorationProfondeur(G, p, parcouru)

G = {   'A': ['C', 'B'], 'B': ['A', 'E'], 'C': ['D', 'B'], 'D': ['C', 'E'],
        'E': [], 'F': ['A', 'C', 'D']}

parcoursProfondeur(G)
