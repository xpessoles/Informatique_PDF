''' 11 - Bases des graphes'''

## 11-3 - A star

## Création de l'image

# Initialisation
import numpy as np
#from 11-Affichage import *
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
ld,cd = 3,7
la,ca = 0,1
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)