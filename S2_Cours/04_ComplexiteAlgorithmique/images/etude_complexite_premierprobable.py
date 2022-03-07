# -*- coding: utf-8 -*-
# Etude de la complexité des différents algorithmes "premierprobable"


import timeit

import pylab
from math import log, exp, floor
from numpy import ones,asarray
from scipy import stats
from pylab import plot,show,savefig,xlabel,ylabel,title,figtext,clf,cla

def expo1(p):
    """Renvoie 2**(p-1) mod p"""
    y = 1
    for i in range(p-1):
        y = 2*y
    return y % p

def expo2(p):
    """Renvoie 2**(p-1) mod p"""
    y = 1
    for i in range(p-1):
        y = (2*y) % p
    return y 

def expo3(p):
    """Renvoie 2**(p-1= mod p par exponentiation rapide"""
    y = 1
    n = p-1
    x = 2
    while n > 0:
        # Invariant : y * (x**n) = 2**(p-1) mod p
        # Variant : n
        if n % 2 != 0: # n est impair
            y = (y * x) % p
            n = n - 1
        # n est pair et y * (x**n) = 2**(p-1) mod p
        x = (x * x) % p
        n = n // 2
    # n == 0 et y = 2 ** (p-1) modulo p
    return y

def premierprobable1(p):
    return expo1(p) == 1

def premierprobable2(p):
    return expo2(p) == 1

def premierprobable3(p):
    return expo3(p) == 1


# nb de répétitions de chaque test pour mesurer le temps
REPEAT=3

def duree(f, x):
  """Calcule le temps mis par Python pour calculer f(x).
  Cette fonction effectue en fait le calcul de f(x) REPEAT fois
  et garde la valeur la plus petite
  (l'idée est d'éliminer les éventuelles perturbations provoquées
  par d'autres processus tournant sur la machine)"""
  t = timeit.Timer(stmt=lambda : f(x))
  time = min(t.repeat(REPEAT, number=1))
  return time


def trace_pp1(N,nom_de_fichier):
    """Trace la duree d'exécution de premierprobable1(p)
       pour p = p_0 / (q**k), k in range(N), en échelle log/log
       Effectue une régression linéaire par moindres carrés"""
    with open(nom_de_fichier+'.csv','w') as f :
        f.write('log10(p=p_0/q**k)'+';'+'log10(T_1(p))\n')
        q = 1.35
        p_zero = 3*(10**5)
        x = []
        y = []
        for k in range(N+1):
            ent = floor(p_zero /(q**k))
            res = duree(premierprobable1,ent)
            x.append(log(ent,10))
            y.append(log(res,10))
            f.write(str(log(ent,10))+';'+str(log(res,10))+'\n')
    x = asarray(x)
    y = asarray(y)
    pente,ordonnee_origine,r,p,sigma = stats.linregress(x,y)
    droite = ordonnee_origine+pente*x 
    plot(x,droite,'r-')
    plot(x,y,'bo')
    xlabel('$\\log_{10}(p)$ avec $p = \\left\\lfloor \\frac{p_0}{q^k} \\right\\rfloor$ et $0 \\leq k \\leq '+str(N)+'$')
    ylabel('$\\log_{10}(T_1(p))$')
    title('Tracé de $T_1$ en échelle logarithmique décimale')
    figtext(0.2,0.7,'Équation : $y = '+str(ordonnee_origine)+\
            ' + '+str(pente)+'\\times x$'+'\n'+'Coefficient de détermination : $'\
            +str(r**2)+'$\n'+'Ici, $p_0 = 3\\times 10^5$ et $q = 1.35$')
    savefig(nom_de_fichier+'.png')
    clf()
    cla()
    return ordonnee_origine,pente,r

def trace_pp2(N, nom_de_fichier):
    """Trace la duree d'exécution de premierprobable2(p)
       pour p = p_0 / (q**k), k in range(N), en échelle log/log
       Effectue une régression linéaire par moindres carrés"""
    with open(nom_de_fichier+'.csv','w') as f :
        f.write('log10(p=p_0/q**k)'+';'+'log10(T_2(p))\n')
        q = 1.35
        p_zero = 10**7
        x = []
        y = []
        for k in range(N+1):
            ent = floor(p_zero /(q**k))
            res = duree(premierprobable2,ent)
            x.append(log(ent,10))
            y.append(log(res,10))
            f.write(str(log(ent,10))+';'+str(log(res,10))+'\n')
    x = asarray(x)
    y = asarray(y)
    pente,ordonnee_origine,r,p,sigma = stats.linregress(x,y)
    droite = ordonnee_origine+pente*x 
    plot(x,droite,'r-')
    plot(x,y,'bo')
    xlabel('$\\log_{10}(p)$ avec $p = \\left\\lfloor \\frac{p_0}{q^k} \\right\\rfloor$ et $0 \\leq k \\leq '+str(N)+'$')
    ylabel('$\\log_{10}(T_2(p))$')
    title('Tracé de $T_2$ en échelle logarithmique décimale')
    figtext(0.2,0.7,'Équation : $y = '+str(ordonnee_origine)+' + '+\
            str(pente)+'\\times x$'+'\n'+'Coefficient de détermination : $'+\
            str(r**2)+'$\n'+'Ici, $p_0 = 10^7$ et $q = 1.35$')
    savefig(nom_de_fichier+'.png')
    clf()
    cla()
    return ordonnee_origine,pente,r

def trace_pp3(N, nom_de_fichier):
    """Trace la duree d'exécution de premierprobable3(p)
       pour p = p_0 / (q**k), k in range(N), en échelle semi-log
       Effectue une régression linéaire par moindres carrés"""
    with open(nom_de_fichier+'.csv','w') as f :
        f.write('log10(p=p_0/q**k)'+';'+'T_3(p)\n')
        q = 140
        p_zero = 10**140
        x = []
        y = []
        for k in range(N+1):
            ent = floor(p_zero /(q**k))
            res = duree(premierprobable3,ent)
            x.append(log(ent,10))
            y.append(res)
            f.write(str(log(ent,10))+';'+str(res)+'\n')
    x = asarray(x)
    y = asarray(y)
    pente,ordonnee_origine,r,p,sigma = stats.linregress(x,y)
    droite = ordonnee_origine+pente*x 
    plot(x,droite,'r-')
    plot(x,y,'bo')
    xlabel('$\\log_{10}(p)$ avec $p = \\left\\lfloor \\frac{p_0}{q^k} \\right\\rfloor$ et $0 \\leq k \\leq '+str(N)+'$')
    ylabel('$T_3(p)$')
    title('Tracé de $T_3$ en échelle semi-logarithmique décimale')
    figtext(0.2,0.7,'Equation : $y = '+str(ordonnee_origine)+' + '+\
            str(pente)+'\\times x$'+'\n'+'Coefficient de détermination : $'+\
            str(r**2)+'$\n'+'Ici, $p_0 = 10^{140}$ et $q = 140$')
    savefig(nom_de_fichier+'.png')
    clf()
    cla()
    return ordonnee_origine,pente,r
