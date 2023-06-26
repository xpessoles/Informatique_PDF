# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:29:39 2021

@author: nicov
"""
import copy


# fruit de type [prix au kilo en euros : int, nom : str, quantité en kg : int]
cueillette = [ [24,"framboises",1], [16,"myrtilles",3], [6,"fraises",5], [3,"mures",2] ]



### question 1
def sac_a_dos(L,capacite):
    """Implémentation de la résolution du problème du sac à dos
    L est une liste des éléments à mettre dans le sac
    capacité est la masse maximale que peut transporter le sac à dos.
    """
    masse_sac = 0
    sac=[]               #à l'initialisation, le sac est vide
    i=0                  #i sert d'indice dans la liste L
    val=0                                 
    while i<len(L) and masse_sac<capacite:#tant qu'on n'a pas parcouru toute la cueillette 
    #et que la masse du sac n'a pas atteint sa capacité                              
        fruit = L[i][:]   
        capacite_restante = capacite - masse_sac                           
        if fruit[-1]>capacite_restante: #si la quantité du i-eme fruit est supérieure à la capacité restante du sac
            fruit[-1]=capacite_restante
        
        #que la quantité correspondant à la capacité restante
        val=val+fruit[0]*fruit[-1]
        sac.append(fruit) #On met le fruit dans le sac
        masse_sac = masse_sac + fruit[-1]    #On calcule la nouvelle masse du sac
        i=i+1  #On incrément i pour passer au fruit suivant de la cueillette
    return sac,val


### question 2
# >>> sac_a_dos(cueillette,5)
# ([[24, 'framboises', 1], [16, 'myrtilles', 3], [6, 'fraises', 1]], 78)

     
        
   
# fruit de type [prix au kilo en euros : int, nom : str, masse en kg : int, quantité : int]
fruits_disponibles = [[3,"melon de cavaillon",1,1], [2.5,"melon jaune",2,1], [2,"pastèque",3,1]]

def sac_a_dos_V2(L,capacite):
    """Implémentation de la résolution du problème du sac à dos
    L est une liste des éléments à mettre dans le sac
    capacité est la masse maximale que peut transporter le sac à dos.
    """
    masse_sac = 0
    sac=[]               #à l'initialisation, le sac est vide
    i=0                  #i sert d'indice dans la liste L
    val=0                                 
    while i<len(L) and masse_sac<capacite:#tant qu'on n'a pas parcouru toute la cueillette 
    #et que la masse du sac n'a pas atteint sa capacité                              
        fruit = L[i][:]   
        capacite_restante = capacite - masse_sac                           
        if fruit[-2]<=capacite_restante: #si la masse du i-eme fruit est inférieur ou égale à la capacité restante du sac
            val=val+fruit[-2]*fruit[0]
            sac.append(fruit) #On met le fruit dans le sac
            masse_sac = masse_sac + fruit[-2]    #On calcule la nouvelle masse du sac
        i=i+1  #On incrément i pour passer au fruit suivant de la cueillette
    return sac,val
    
# test
# >>> sac_a_dos_V2(fruits_disponibles,5)
# ([[3, 'melon de cavaillon', 1, 1], [2.5, 'melon jaune', 2, 1]], 8.0)


### question 4
# La solution S=[[2.5,'melon jaune',2,1],[2,'pastèque',3,1]]
# la capacité du sac n'est pas dépassée
# donne une valeur au sac de 2*2.5+3*2=11 contre 8 avec l'algorithme

### question 5
# La propriété du choix glouton est respectée mais pas celle de la sous-structure optimale

### exercice 2 PCA
# 8h45 est représenté par un flottant 8.45
L=[[8,9,"C1"],[8.45,10.3,"C2"],[8.1,11.3,"C3"],[11.15,11.45,"C4"],[12,12.45,"C5"],[11,13,"C6"], [12.3,14,"C7"],[16,17,"C8"],[15,18,"C9"],[16.2,18.15,"C10"]]

### question 1
S=[[8,9,"C1"],[11.15,11.45,"C4"],[12,12.45,"C5"],[16,17,"C8"]]

### question 2
def choix_conference(C:list)->list:
    resultat=[C[0]]
    Fin=resultat[-1][1]
    for element in C[1:]:
        if element[0]>=Fin:
            resultat.append(element)
            Fin=resultat[-1][1]
    return resultat
        
# >>> choix_conference(L)
# [[8, 9, 'C1'], [11.15, 11.45, 'C4'], [12, 12.45, 'C5'], [16, 17, 'C8']]


### question 3
def choix_conference_recursif(C:list,k:int,n:int)->list:
    '''k est l'indice du dernier élément de C, n est la taille de la liste. Au premier appel, k=n-1'''
    if k==0:
        return [C[0]]
    resultat=choix_conference_recursif(C,k-1,n) # k est le paramètre qui varie
    m=k # m est l'indice de la conférence, il commence à k pour ne pas tout reprendre à 0
    Fin=resultat[-1][1]
    while m<n and C[m][0]<Fin: # m est l'indice de la conférence
        m=m+1
    if m<n:
        resultat.append(C[m])
        k=m
    return resultat
    
# >>> choix_conference_recursif(L,len(L)-1,len(L))
# [[8, 9, 'C1'], [11.15, 11.45, 'C4'], [12, 12.45, 'C5'], [16, 17, 'C8']]
            
    




        

        
        
        
        
        