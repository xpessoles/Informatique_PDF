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
# def creation_grille(p: float, n: int) -> list :

#Q2
# def percolation(grille : list) -> None:

#Q03

#Q04
#def teste_percolation(p : float, n : int) -> bool:
 
#Q05
# def proba(p, k=20, n=128) -> float:
 
# Q06
# def tracer_proba(n,nom_de_fichier):
 