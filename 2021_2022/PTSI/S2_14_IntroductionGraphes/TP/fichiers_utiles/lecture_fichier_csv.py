### TD01 le tri
### algorithme de tri

from tris import *
import random as rd
import time as t
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)


### lecture du fichier csv

f=open('films_martiniere.csv','r')
ligne1=f.readline()
fichier=f.readlines()
f.close()

L=[]
for ligne in fichier:
    ligne=ligne.replace('"','')
    ligne=ligne.split(';')
    ligne[-1]=ligne[-1].rstrip('\n')
    ligne[-1]=int(ligne[-1])
    ligne[1]=int(ligne[1])
    L.append(ligne)
    





