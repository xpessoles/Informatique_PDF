''' 11 - Bases des graphes'''

## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 13,7 # Pas moins de 10,10
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

Image[0:6,0] = Noir
Image[0:4,1] = Noir
Image[0:1,3] = Noir
Image[0:2,4] = Noir
Image[0:4,5] = Noir
Image[0:6,6] = Noir

Image[11:,0] = Noir
Image[10:,1] = Noir
Image[9:,2] = Noir
Image[8:,3] = Noir
Image[9:,4] = Noir
Image[10:,5] = Noir
Image[11:,6] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 9,6
la,ca = 9,0
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)