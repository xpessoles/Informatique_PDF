''' 11 - Bases des graphes'''

## 11-3 - A star

## Dijkstra

'''Version avec une file'''

# Initialisation

Image_Anim = Image.copy() # Si animation
Distances = np.inf*np.ones([Nl,Nc])
Distances[ld,cd] = 0
Provenances = {}

Traites = []
File = [(ld,cd)]

# Itérations

S = (ld,cd)
lS,cS = ld,cd
it = 0
while len(File) > 0 and S!=Arrivee and Distances[lS,cS]!=np.inf:
    it += 1
    # S ← Station parmi File ayant la distance minimum dans Distances
    Min = np.inf
    for s in File:
        l,c = s
        d = Distances[l,c]
        if d <= Min:
            Min = d
            S = s
    lS,cS = S
    # Mise à jour de File
    File.remove(S)
    '''
    # Affichage animation
    Image_Anim[lS,cS] = Rouge
    Chemin = "Animations/Dijkstra/"+str(it)+".png"
    Affiche_Save(12,Image_Anim,True,Chemin)
    #Affiche(12,Image_Anim,True)
    '''
    # Voisins ← Dico des stations voisines de S non traitées
    Voisins = Dico_Voisins[S]
    for V in Voisins:
        cle,_ = V
        ''''''
        if cle in Traites:  # Lire remarque
            Voisins.remove(V)
        ''''''
    # Mise à jour de traite
    Traites.append(S)
    # Traitement des voisins
    for V in Voisins:
        Case_v,dv = V
        if Case_v not in File:
            File.append(Case_v)
        lv,cv = Case_v
        D_S_V = Distances[lS,cS] + dv
        D_V = Distances[lv,cv]
        if D_S_V < D_V:
            Distances[lv,cv] = D_S_V
            Provenances[Case_v] = S

'''
Remarque:
Comme dit dans le cours, pour Dijkstra, on améliore les choses incluant dans Voisins  les voisins déjà traités
'''

# Traitement final C

Dst = Distances[la,ca]
print('Distance: ',Dst)
print('Itérations: ',it)

if Dst==np.inf:
    print("Pas de chemin possible")
else:
    p = Arrivee
    Chemin_Djk = [p]
    while p != Depart:
        p = Provenances[p]
        Chemin_Djk.append(p)
    Chemin_Djk.reverse()
    print(Chemin_Djk)

# Affichage du chemin

Image_Djk = Image.copy()
if Dst!=np.inf:
    Vert = [0,255,0]
    for Case in Chemin_Djk:
        l,c = Case
        Image_Djk[l,c] = Vert
        Image_Anim[l,c] = Vert # Si animation

Affiche(10,Image_Djk,False)
plt.savefig('Res_Solution_Djk.png')

'''
Chemin = "Animations/Dijkstra/"+str(it+1)+".png"
Affiche_Save(12,Image_Anim,True,Chemin)
'''

# Affichage des distances

Affiche_Degrade(11,Distances)
plt.savefig('Res_Distances_Djk.png')
