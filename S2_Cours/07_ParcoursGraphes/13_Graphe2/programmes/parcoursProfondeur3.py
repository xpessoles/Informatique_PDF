def explorationProfondeur(G, s, parcouru):
    parcouru[s] = True
    for ss in G[s]: # G[s] liste des successeurs de s dans G
        if not parcouru[ss]:
            explorationProfondeur(G, ss, parcouru) # appel récursif

def parcoursProfondeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(G, r, parcouru)

def explorationProfondeur(G, s, parcouru):
    print(s)
    parcouru[s] = True
    for ss in G[s]: # G[s] liste des successeurs de s dans G
        if not parcouru[ss]:
            explorationProfondeur(G, ss, parcouru) # appel récursif

def parcoursProfondeur(G):
    parcouru = {}   # dictionnaire de booléens pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        parcouru[s] = False
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if not parcouru[r]:
            explorationProfondeur(G, r, parcouru)

G = {   'A': ['C', 'B'], 'B': ['A', 'E'], 'C': ['D', 'B'], 'D': ['C', 'E'],
        'E': [], 'F': ['A', 'C', 'D']}

parcoursProfondeur(G)
