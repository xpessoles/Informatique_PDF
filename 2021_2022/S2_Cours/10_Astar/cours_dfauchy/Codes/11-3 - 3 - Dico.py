''' 11 - Bases des graphes'''

## 11-3 - A star

## Dictionnaire

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
                    Di = sqrt((li-l)**2+(ci-c)**2)
                    Couple = [Case_i,Di]
                    Dico_Voisins[Case].append(Couple)

# Remplissage de Dico_Voisins

for Case in Dico_Voisins.keys():
    l,c = Case
    Pix = Image[l,c]
    Couples_Voisins(l,c)

''' Possible version sur l et c
for l in range(Nl):
    for c in range(Nc):
        Pix = Image[l,c]
        if Test_Pix(Pix,Noir)==False:
            Couples_Voisins(l,c)
'''