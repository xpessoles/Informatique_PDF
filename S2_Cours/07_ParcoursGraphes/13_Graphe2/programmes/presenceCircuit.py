def presenceCircuit(G):
    def explorationProfondeur(s):
        etat[s] = 'découvert'
        for ss in G[s]: # G[s] liste des successeurs de s dans G
            if etat[ss] == 'attente':
                return explorationProfondeur(ss) # appel récursif
            elif etat[ss] == 'découvert':
                return True
        etat[s] = 'exploré'
        return False
    etat = {}      # dictionnaire de chaine de caractères pour le marquage
    for s in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        etat[s] = 'attente'
    for r in G.keys(): # Itération sur les clés de G (dictionnaire de listes)
        if etat[r] == 'attente':
            if explorationProfondeur(r):
                return True
    return False

G = {   'a': ['b'], 'b': ['c', 'd'], 'c': ['e'], 'd': ['e'], 'e': []}
print(presenceCircuit(G))

G = {   'a': ['b'], 'b': ['c', 'd'], 'c': ['e'], 'd': ['e'], 'e': ['a']}
print(presenceCircuit(G))