''' 11 - Bases des graphes'''

'''Dossier partagé images: https://www.dropbox.com/sh/pe158jwai7yqkol/AAA3N3sptIYvkH64A90r2DUqa?dl=0'''

## 11-3 - A star

## Création de l'image

# Image

Lab = plt.imread("Labyrinthe_Grand.bmp")
Nl,Nc = Lab.shape[0:2]

def f_NB(im):
    Nl,Nc = im.shape[0:2]
    IM_Mono = np.copy(im)
    for x in range(Nc):
        for y in range(Nl):
            R,G,B = im[y,x]
            kR = 0.5
            kG = 0.4
            kB = 0.1
            Nuance = kR * R + kG * G + kB * B
            if Nuance < 127:
                Val = 0 # Noir
            else:
                Val = 255 # Blanc
            Px_New = [Val,Val,Val]
            IM_Mono[y,x] = Px_New
    return IM_Mono

Image = f_NB(Lab)

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 5,0
la,ca = 175,540
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)