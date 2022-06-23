''' 11 - Bases des graphes'''

## 11-3 - A star

## Affichage

import matplotlib.pyplot as plt
plt.close('all')
import numpy as np

def Affiche(fig,im,grille):
    Nl,Nc = im.shape[0:2]
    plt.figure(fig)
    plt.imshow(im)
    plt.axis('scaled')
    plt.xlim([-0.5,Nc-0.5])
    plt.ylim([Nl-0.5,-0.5])
    plt.grid(grille)
    if grille==True:
        Lx = [str(i) for i in range(Nc+1)]
        Ly = [str(i) for i in range(Nl+1)]
        plt.xticks(np.arange(-0.5,Nc+0.5,1),Lx)
        plt.yticks(np.arange(-0.5,Nl+0.5,1),Ly)
    else:
        plt.axis('off')
    plt.show()
    plt.pause(0.00001)

def Affiche_Save(fig,im,grille,chemin): # Nécessaire pour éviter bug redimensionnement
    Nl,Nc = im.shape[0:2]
    plt.figure(fig)
    plt.imshow(im)
    plt.axis('scaled')
    plt.xlim([-0.5,Nc-0.5])
    plt.ylim([Nl-0.5,-0.5])
    plt.grid(grille)
    if grille==True:
        Lx = [str(i) for i in range(Nc+1)]
        Ly = [str(i) for i in range(Nl+1)]
        plt.xticks(np.arange(-0.5,Nc+0.5,1),Lx)
        plt.yticks(np.arange(-0.5,Nl+0.5,1),Ly)
    else:
        plt.axis('off')
    plt.savefig(chemin)

def Affiche_Degrade(Fig,Tab):
    Nl,Nc = np.shape(Tab)
    x,y = range(0,Nc),range(0,Nl)
    plt.figure(Fig)
    plt.clf()
    plt.contourf(x,y,Tab,1000) # 1000 nombre de couleurs
    plt.colorbar() # Le max de la colorbar est défini lors de son appel sur le champ affiché
    plt.axis('scaled')
    plt.xlim([-0.5,Nc-0.5])
    plt.ylim([Nl-0.5,-0.5])
    plt.show()
    plt.pause(0.00001)
