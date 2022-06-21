''' 11 - Bases des graphes'''

'''Dossier partagé images: https://www.dropbox.com/sh/pe158jwai7yqkol/AAA3N3sptIYvkH64A90r2DUqa?dl=0'''

## 11-3 - A star

## Création de l'image

# Image

Res = plt.imread("Réseau.bmp")
Nl,Nc = Res.shape[0:2]

def f_NB(im):
    Nl,Nc = im.shape[0:2]
    IM_Mono = np.copy(im)
    for x in range(Nc):
        for y in range(Nl):
            R,G,B = im[y,x]
            kR = 0.33
            kG = 0.33
            kB = 0.34
            Nuance = kR * R + kG * G + kB * B
            if Nuance < 200:
                Val = 255 # Blanc
            else:
                Val = 0 # Noir
            Px_New = [Val,Val,Val]
            IM_Mono[y,x] = Px_New
    return IM_Mono

Image = f_NB(Res)

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
ld,cd = 416,99
la,ca = 16,242
Rouge = [255,0,0]
Image[ld,cd] = Rouge
Bleu = [0,0,255]
Image[la,ca] = Bleu

Depart = (ld,cd)
Arrivee = (la,ca)

# Affichage

Affiche(1,Image,True)