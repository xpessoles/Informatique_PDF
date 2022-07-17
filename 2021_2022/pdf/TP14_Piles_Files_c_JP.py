## Q1a

# On cree une pile ouvert qui contient les indices des parentheses ouvrantes et une parenthese fermee ferme la dernière ouverte c'est-a-dire la pile de la liste ouvert.

from collections import deque

def parentheses(s:str)->list:
    ouvert=deque()
    L=[]
    n=len(s)
    for i in range(n):
        if s[i]=="(":
            ouvert.append(i)
        elif s[i]==")":
            L.append([ouvert.pop(),i])
    return(L)

## Q1b

# il faut même nombre de ( que de )
# L'idée est d'empiler quand on trouve une ( et de dépiler si on trouve une ).
# Ce sera bien parenthésé si à la fin, la pile est vide, mais pas avant.

# def bien_parentheses(s):
#     n=len(s)
#     f,o=0,0
#     i=0
#     while i<=n-1 and f<=o:
#         if s[i]=="(":
#             o+=1
#         else:
#             f+=1
#         i=i+1
#     return(f==o and i==n)

def bien_parentheses(s):
    n=len(s)
    pile=deque()
    if s[0]=="(":
        pile.append(0)
    else:
        return False
    i=1
    while i<=n-1 and len(pile)!=0:
        if s[i]=="(":
            pile.append(i)
        else:
            pile.pop()
        i=i+1
    return(i==n and len(pile)==0)

## Q1c

# On crée 3 listes a,c,p contenant  les {,[ et (.

def parentheses2(s:str)->list:
    a,c,p=deque(),deque(),deque()
    L=[]
    n=len(s)
    for i in range(n):
        if s[i]=="(":
            p.append(i)
        elif s[i]=="[":
            c.append(i)
        elif s[i]=="{":
            a.append(i)
        elif s[i]==")":
            L.append([p.pop(),i])
        elif s[i]=="]":
            L.append([c.pop(),i])
        elif s[i]=="}":
            L.append([a.pop(),i])
    return(L)


## Q1d

# il faut même nombre de ( que de )
# Il faut qu'a chaque rang, le nombre de ( soit supérieur au nombre de ).
# Inutile d'utiliser une pile.

s="((())()())"

# o représente la pile des parenthèses ouvrantes.


def parentheses_rec_int(s:str,i:int,o:list)->list:
    n=len(s)
    if i==n-1:
        return [[o.pop(),n-1]]
    elif s[i]=="(":
        return parentheses_rec_int(s,i+1,o+[i])
    elif s[i]==")":
        return [[o.pop(),i]]+ parentheses_rec_int(s,i+1,o)


def parentheses_rec(s):
    L=[]
    return(parentheses_rec_int(s,0,L))



## Q2

def inversion(pile):
    a=pile.pop()
    b=pile.pop()
    pile.append(a)
    pile.append(b)
    return(pile)

## Q3


# On enlève le k ieme élément en partant du sommet, les autres elements restent en place.

def depilenumero(pile,k):
    depile=deque()
    for i in range(k):
        depile.append(pile.pop())
    element=depile.pop()
    for i in range(len(depile)):
        pile.append(depile.pop())
    return(pile, element)

## Q4

def lirelenumero(pile,n):
    p=len(pile)
    if n>p:
        return("taille insuffisante")
    else:
        return(pile[p-n])

## Q5

# Pour conserver l'ordre, on dépile 2 fois.

pile=[7,5,4,3,8,6,7,4,6,9,0,7,6]


def inversionextreme(pile):
    depile=[]
    p=len(pile)
    top=pile.pop()
    for i in range(p-2):
        depile.append(pile.pop())
    tip=pile.pop()
    print(pile)
    pile.append(top)
    for i in range(p-2):
        pile.append(depile.pop())
    pile.append(tip)
    return(pile)

# Complexité quadratique.

## Q6

def inversion(pile):
    depile=[]
    for i in range(len(pile)):
        depile.append(pile.pop())
    return(depile)

## Q7

# si on autorise, la complexité est linéaire, sinon elle est quadratique.


def inversion_garde(pile):  # On conserve la pile.
    depile=[]
    for i in range(len(pile)):
        x=pile[-i-1]
        depile.append(x)
    return(depile)

## Q8

def couper(pile,k):
    depile=[]
    for i in range(k):
        depile.append(pile.pop())
    return(depile)
