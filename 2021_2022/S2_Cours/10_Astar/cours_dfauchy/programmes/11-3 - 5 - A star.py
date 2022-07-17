''' 11 - Bases des graphes'''

## 11-3 - A star

## Algorithme A*

# Initialisation

Image_Anim = Image.copy() # Si animation
Distances = np.inf*np.ones([Nl,Nc])
Distances[ld,cd] = 0
Reste = Dico_Voisins.copy()
Provenances = {}

# f

from math import sqrt
def f(l,c):
    d_deb = Distances[l,c]
    d_fin = sqrt((l-la)**2+(c-ca)**2)
    heuristique = d_deb + d_fin
    return heuristique

# Itérations

S = (ld,cd)
lS,cS = ld,cd
it = 0
while len(Reste) > 0 and S!=Arrivee and Distances[lS,cS]!=np.inf:
    it += 1
    # S ← Station parmi Reste ayant la distance minimum dans Distances
    Min = np.inf
    for s in Reste:
        l,c = s
        d = f(l,c) ###
        if d <= Min:
            Min = d
            S = s
    lS,cS = S
    # Mise à jour de Reste
    del Reste[S]
    '''
    # Affichage animation
    Image_Anim[lS,cS] = Rouge
    Chemin = "Animations/A star/"+str(it)+".png"
    Affiche_Save(22,Image_Anim,True,Chemin)
    #Affiche(22,Image_Anim,True)
    '''
    # Voisins ← Dico des stations de Reste voisines de S
    Voisins = Dico_Voisins[S]
    for V in Voisins:
        cle,_ = V
        if cle not in Reste.keys():
            Voisins.remove(V)
    # Traitement des voisins
    for V in Voisins:
        Case_v,dv = V
        lv,cv = Case_v
        D_S_V = Distances[lS,cS] + dv
        D_V = Distances[lv,cv]
        if D_S_V < D_V:
            Distances[lv,cv] = D_S_V
            Provenances[Case_v] = S

# Traitement final C

Dst = Distances[la,ca]
print('Distance: ',Dst)
print('Itérations: ',it)

if Dst==np.inf:
    print("Pas de chemin possible")
else:
    p = Arrivee
    Chemin_Astar = [p]
    while p != Depart:
        p = Provenances[p]
        Chemin_Astar.append(p)
    Chemin_Astar.reverse()
    print(Chemin_Astar)

# Affichage du chemin

Image_Astar = Image.copy()
if Dst!=np.inf:
    Violet = [238,130,238]
    for Case in Chemin_Astar:
        l,c = Case
        Image_Astar[l,c] = Violet
        Image_Anim[l,c] = Violet # Si animation

Affiche(20,Image_Astar,False)
plt.savefig('Res_Solution_Astar.png')

'''
Chemin = "Animations/A star/"+str(it+1)+".png"
Affiche_Save(22,Image_Anim,True,Chemin)
'''

# Affichage des distances

Affiche_Degrade(21,Distances)
plt.savefig('Res_Distances_Astar.png')

## Comparaison des chemins Dijkstra Astar

if 'Chemin_Djk' in globals():
    Image_Djk_Astar = Image.copy()
    if Dst!=np.inf:
        Vert = [0,255,0]
        for Case in Chemin_Djk:
            l,c = Case
            Image_Djk_Astar[l,c] = Vert
        Violet = [238,130,238]
        for Case in Chemin_Astar:
            l,c = Case
            Image_Djk_Astar[l,c] = Violet
    Affiche(30,Image_Djk_Astar,False)
    plt.savefig('Res_Dijstra_Astar.png')