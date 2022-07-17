''' 11 - Bases des graphes'''

## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 50,50 # Pas moins de 10,10
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

Val = 1
Image[Val,Val:] = Noir
Image[Val:,Val] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 0,0
la,ca = Nl-2,Nc-1
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = str(ld) + '-' + str(cd)
Arrivee = str(la) + '-' + str(ca)

# Affichage

Affiche(1,Image,True)