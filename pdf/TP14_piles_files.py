# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

chaine='(()()())'

# def parentheses(s:str)->list:
#     ouvrante = ()
#     sortante = ()
#     ind=0
#     for x in s:
#         if x=='(':
#             ouvrante.append(ind)
#         else:
#             sortante.append(ind)
#         ind+=1
#     return (ouvrante,sortante)
#

def parentheses(s:str)->list:
    pile=deque()
    L=[]
    i=0
    for x in s:
        if x=='(':
            pile.append(i)
        else:
            j=pile.pop()
            L.append(j,i)
        i+=1
    return L



### TD1 piles
def creer_pile(t):
    return []

def est_vide(p):
    return len(p)==0

def empiler(p,e):
    p.append(e)

def depiler(p):
    assert len(p)>0
    return p.pop()


### exercice 1 : la parenthese inattendue
### exemple '(())()' les couples correspondant (0,3),(1,2),(4,5)

#question 1
def parentheses(s):
    ''' fonction renvoyant les couples indices ( )'''
    p=creer_pile(len(s))
    for i in range(len(s)):
        if s[i]=='(':
            empiler(p,i)
        else:
            if est_vide(p):
                return False
            else:
                j=depiler(p)
                print ((j,i))
    return est_vide(p)

# >>> parentheses('(())()')
# (1, 2)
# (0, 3)
# (4, 5)
# True

# question 2
# creation de deux listes 'ouvert' et 'ferme' qui doivent être la longeur de la chaine, l'indice 0 est le premier élément de la liste 'ouvert' et dont la succession d'indices doit respecter
def parentheses1(s):
    ''' s est composé de ('''
    ouvert=[None]*len(s)
    ferme=[None]*len(s)
    for i in range(len(s)):
        if s[i]=='(':
            ouvert[i]=1
        else:
            ferme[i]=1
    if ouvert[0]==None or ferme[-1]==None:
        return False
    else:
        nb=1
        for j in range(1,len(s)):
            if ouvert[j]==1:
                nb=nb+1
            else:
                if ferme[j]==1:
                    nb=nb-1
                    if nb==-1:
                        return False
                else:
                    return False
    return nb==0

# >>> parentheses1('(())()')
# True
# >>> parentheses1('((())()')
# False
# >>> parentheses1(')(())()')
# False
# >>> parentheses1('(())()(')
# False




# question 3
def parentheses2(s):
    ''' fonction renvoyant les couples indices ( )'''
    p=creer_pile(len(s))
    c=creer_pile(len(s))
    a=creer_pile(len(s))
    for i in range(len(s)):
        if s[i]=='(':
            empiler(p,i)
        elif s[i]=='[':
            empiler(c,i)
        elif s[i]=='{':
            empiler(a,i)
        elif s[i]==')':
            if est_vide(p):
                return False
            else:
                j=depiler(p)
                print ((j,i))
        elif s[i]==']':
            if est_vide(c):
                return False
            else:
                j=depiler(c)
                print ((j,i))
        else:
            if est_vide(a):
                return False
            else:
                j=depiler(a)
                print ((j,i))
    return (est_vide(p) and est_vide(c) and est_vide(a))

# >>> parentheses2('(())()[[{}()]]')
# (1, 2)
# (0, 3)
# (4, 5)
# (8, 9)
# (10, 11)
# (7, 12)
# (6, 13)
# True

# >>> parentheses2('(()()[[}()]]')
# (1, 2)
# (3, 4)
# False


### question 4 : parentheses et autres caractères
def parentheses3(s):
    ''' fonction renvoyant les couples indices ( )'''
    p=creer_pile(len(s))
    for i in range(len(s)):
        if s[i]=='(':
            empiler(p,i)
        elif s[i]==')':
            if est_vide(p):
                return False
            else:
                j=depiler(p)
                print ((j,i))
    return est_vide(p)

# >>> parentheses3('((10-6)**5)*(2+3)')
# (1, 6)
# (0, 10)
# (12, 16)
# True

#def parentheses_rec(s):
def parentheses_rec(chaine,nb):
    if nb<0:
        return False
    if len(chaine)==0:
        return nb==0
    if chaine[0]=='(':
        return (parentheses_rec(chaine[1:],nb+1))
        if chaine[0]==')':
            return (parentheses_rec(chaine[1:],nb-1))


# >>> parentheses_rec('(()())',0)
# True
# >>> parentheses_rec('(()))',0)
# False

### exercice 2 - inversion
def inversion(p):
    e=depiler(p)
    f=depiler(p)
    empiler(p,e)
    empiler(p,f)
    return p

# >>> inversion([1,2,3,4,5,6])
# [1, 2, 3, 4, 6, 5]

### exercice 3 - dépile le nieme
def depile_3(p):
    mem=[]
    for i in range(len(p)-2):
        mem.append(depiler(p))
    return mem[-1]

# >>> depile_3([1,3,9,5,1,6,7])
# 9

### exercice 4 - lire le nieme on depile et rempile ou on va chercher l'élément de l'indice désiré ????
def lire(p,n):
    if len(p)<n:
        print ('la pile n\'a pas n éléments')
    else:
        mem=[]
        for i in range(len(p)-n):
            mem.append(depiler(p))
            nieme=mem[-1]
        for j in range(len(mem)):
            p.append(depiler(mem))
    return nieme

# >>> lire([1,3,9,5,1,6,7],5)
# 6

### exercice 5 - Inversion des extrêmes
def inversion_ext(p):
    mem=[]
    ext=p[-1]
    while est_vide(p)==False:
        mem.append(depiler(p))
    p.append(ext)
    for i in range(len(mem)-1):
        p.append(depiler(mem))
    return p

# >>> inversion_ext([1,3,9,5,1,6,7])
# [7, 1, 3, 9, 5, 1, 6]

### exercice 6 - Inversion de pile
def renverse(p):
    mem=[]
    while est_vide(p)==False:
        mem.append(depiler(p))
    return (mem)

# >>> renverse([1,3,9,5,1,6,7])
# [7, 6, 1, 5, 9, 3, 1]

### exercice 7 - Tu coupes ?
import random as rd
def couper(p):
    n=rd.randint(1,len(p))
    mem=[]
    for i in range(n):
        mem.append(depiler(p))
    return mem

# >>> couper([1,3,9,5,1,6,7])
# [7, 6, 1]

### exercice 8 - Mélange de cartes
def melange(p,q):
    mem=[]
    while est_vide(p)==False and est_vide(q)==False:
        if rd.randint(0,1)==1:
            mem.append(depiler(p))
        else:
            mem.append(depiler(q))
    if est_vide(p)==False:
        for i in range(len(p)):
            mem.append(depiler(p))
    else:
        for i in range(len(q)):
            mem.append(depiler(q))
    return mem

# >>> melange([1,2,3,4,5,6],[10,12,14,15])
# [15, 6, 5, 4, 3, 14, 2, 12, 1, 10]





