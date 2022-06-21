''' 11 - Bases des graphes'''

## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 13,10 # Pas moins de 10,10
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

Image[0:9,0:3] = Noir
Image[0:6,3] = Noir
Image[0:4,4] = Noir
Image[0,6] = Noir
Image[0:2,7] = Noir
Image[0:4,8] = Noir
Image[0:6,9] = Noir

Image[12:,8] = Noir
Image[11:,9] = Noir

Image[9:,0:6] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 11,8
la,ca = 8,3
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)