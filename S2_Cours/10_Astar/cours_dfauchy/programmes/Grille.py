''' 11 - Bases des graphes'''
from Affichage import *
## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 5,9
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

for l in range(1,4):
    Image[l,4] = Noir

for c in range(4,6):
    Image[1,c] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
lD,cD = 3,7
lA,cA = 0,1
Rouge = [255,0,0]
Image[lD,cD] = Rouge
Bleu = [0,0,255]
Image[lA,cA] = Bleu

Depart = (lD,cD)
Arrivee = (lA,cA)

# Affichage

Affiche(1,Image,True)




###Heuristique

# Distances = np.inf*np.ones([Nl,Nc])
# Distances[ld,cd] = 0

from math import sqrt
def f(l,c,la,ca):
    d_deb = Distances[l,c]
    d_fin = sqrt((l-la)**2+(c-ca)**2)
    heuristique = d_deb + d_fin
    return heuristique

def f_fin(l,c,la,ca):
    d_fin = sqrt((l-la)**2+(c-ca)**2)
    heuristique = d_fin
    return int(heuristique*10)

def f_man(l,c,la,ca):
    dec=min(abs(l-la),abs(c-ca))
    if l==la or c==ca:
        d_fin = 10*(abs(l-la))+10*(abs(c-ca))
    else:
        d_fin = 10*(abs(l-la)-dec)+10*(abs(c-ca)-dec)+dec*14
    return d_fin



Affiche_distance(1,Image,True,f_man,Arrivee)


# Fonction de comparaison de pixels

def Test_Pix(P1,P2):
    Res = True
    for i in range(3):
        Test = P1[i]==P2[i]
        Res = Res & Test
    return Res

# Initialisation de Dico_Voisins

Noir = [0,0,0]
Dico_Voisins = {}
for l in range(Nl):
    for c in range(Nc):
        Pix = Image[l,c]
        Case = (l,c)
        if Test_Pix(Pix,Noir)==False:
            Dico_Voisins[Case] = []


# Fonction de traitement des voisins d'une case

from math import sqrt

def Couples_Voisins(l,c):
    Case = (l,c)
    for li in range(l-1,l+2):
        for ci in range(c-1,c+2):
            Case_i = (li,ci)
            # Ne pas traiter la case actuelle
            test_case = (Case_i != Case)
            # Etre dans l'image
            test_image = (0 <= li < Nl and 0 <= ci < Nc)
            if test_case and test_image:
                Pixi = Image[li,ci]
                if Test_Pix(Pixi,Noir)==False:
                    Di = int(sqrt((li-l)**2+(ci-c)**2)*10)
                    Couple = [Case_i,Di]
                    Dico_Voisins[Case].append(Couple)

# Remplissage de Dico_Voisins

for Case in Dico_Voisins.keys():
    l,c = Case
    Pix = Image[l,c]
    Couples_Voisins(l,c)



Reste = Dico_Voisins.copy()
S = (lD,cD)

#Initialisation ds distances

Distances = np.inf*np.ones([Nl,Nc])
Distances[lD,cD] = 0


lS,cS = lD,cD
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