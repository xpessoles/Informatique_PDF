import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from matplotlib.colors import ListedColormap

#Q1
def creation_grille(p, n):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if rand() < p:
                grille[i][j] = 1.
    return grille



#Q2
echelle = ListedColormap(['black', 'aqua', 'white'])
def afficher_grille(grille,nom_de_fichier):
    plt.matshow(grille,cmap=echelle)
    plt.colorbar()
    plt.savefig(nom_de_fichier)
    return None

afficher_grille(creation_grille(0.6, 10),'tp09_Q02_durif.png')

#Q3
def percolation(grille):
    n, p = grille.shape
    lst = []
    for j in range(p):
        if grille[0][j] == 1.: # les cases vides de la première ligne
            grille[0][j] = .5 # sont remplies et ajoutées à lst
            lst.append((0, j))
    while len(lst) > 0:
        (i, j) = lst.pop() # une case est extraite de lst
        if i > 0 and grille[i-1][j] == 1.: # si le voisin haut est vide, il est rempli
            grille[i-1][j] = .5
            lst.append((i-1, j))
        if i < n-1 and grille[i+1][j] == 1.: # si le voisin bas est vide, il est rempli
            grille[i+1][j] = .5
            lst.append((i+1, j))
        if j > 0 and grille[i][j-1] == 1.: # si le voisin gauche est vide, il est rempli
            grille[i][j-1] = .5
            lst.append((i, j-1))
        if j < p - 1 and grille[i][j+1] == 1.: # si le voisin droit est vide, il est rempli
            grille[i][j+1] = .5
            lst.append((i, j+1))

#Q04
grille = creation_grille(.61, 64)
grille_percolee = grille.copy()
percolation(grille_percolee)
fig1 = plt.matshow(grille, cmap=echelle)
plt.axis('off')
fig2 = plt.matshow(grille_percolee, cmap=echelle)
plt.axis('off')
plt.savefig('tp09_Q04_durif.png')

#Q05
def teste_percolation(p, n):
    grille = creation_grille(p, n)
    percolation(grille)
    for j in range(n):
        if grille[n-1][j] == .5:
            return(True)
    return(False)


#Q06

def proba(p, k=20, n=128):
    s = 0
    for i in range(k):
        if teste_percolation(p, n):
            s += 1
    return s/k

#Q07
def tracer_proba(n,nom_de_fichier):
    x=np.linspace(0,1,21)
    y=[]
    for p in x:
        y.append(proba(p,20,n))
    plt.clf()
    plt.plot(x,y)
    plt.savefig(nom_de_fichier)
    return None


