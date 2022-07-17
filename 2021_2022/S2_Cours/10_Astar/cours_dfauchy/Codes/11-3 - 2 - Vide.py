''' 11 - Bases des graphes'''

## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 50,50
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

# RAS

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 0,0
la,ca = Nl-1,Nc-1
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)