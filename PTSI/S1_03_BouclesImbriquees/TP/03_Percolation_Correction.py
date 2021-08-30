# === Import des modules ===
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from matplotlib.colors import ListedColormap

# === Fonctions prédéfinies ===
def sauvegarder_grille(grille : list, nom_de_fichier : str) -> None:
    echelle = ListedColormap(['black', 'aqua', 'white'])
    plt.matshow(grille,cmap=echelle)
    plt.colorbar()
    plt.savefig(nom_de_fichier)
    return None

def afficher_grille(grille : list) -> None:
    echelle = ListedColormap(['black', 'aqua', 'white'])
    plt.matshow(grille,cmap=echelle)
    plt.colorbar()
    plt.show()
    return None
# ==============================

#Q1
def creation_grille(p: float, n: int) -> list :
    grille =  []
    for i in range(n) :
        ligne = []
        for j in range(n) :
            if rand() < p :
                ligne.append(1.)
            else :
                ligne.append(0)
        grille.append(ligne)
    return grille

# afficher_grille(creation_grille(0.6, 10))


#Q2
def percolation(grille : list) -> None:
    n = len(grille)
    p = len(grille[0])
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

#Q03
grille = creation_grille(.6, 64)
grille_percolee = grille.copy()
percolation(grille_percolee)
afficher_grille(grille_percolee)


#Q04
def teste_percolation(p : float, n : int) -> bool:
    grille = creation_grille(p, n)
    percolation(grille)
    for j in range(n):
        if grille[n-1][j] == .5:
            return(True)
    return(False)


#Q05
def proba(p, k=20, n=128) -> float:
    s = 0
    for i in range(k):
        if teste_percolation(p, n):
            s += 1
    return s/k

#Q06
def tracer_proba(n,nom_de_fichier):
    x=np.linspace(0,1,21)
    y=[]
    for p in x:
        y.append(proba(p,20,n))
    plt.clf()
    plt.plot(x,y)
    #plt.savefig(nom_de_fichier)
    plt.show()
    return None
tracer_proba(128,"vide")

