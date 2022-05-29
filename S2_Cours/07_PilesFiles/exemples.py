#Pile
#Exemple 1

from collections import deque

pile = deque()
for i in range(10):
    pile.append(i)


def copy_pile(pile):
    pile_tmp = deque()
    pile_copy = deque()

    while pile :
        pile_tmp.append(pile.pop())

    while pile_tmp :
        el= pile_tmp.pop()
        pile.append(el)
        pile_copy.append(el)
    return pile_copy


#Exemple 2


def hauteur(pile) -> int :
    pile_temp = deque()
    h = 0
    while pile :
        pile_temp.append(pile.pop())
        h = h+1
    while pile_temp :
        pile.append(pile_temp.pop())
    return h

def hauteur_rec(pile):
    if not pile :
        return 0
    else :
        pile.pop()
        return 1+hauteur_rec(pile)


#Exemple3

def reverse(pile):
    pile_tmp = deque()
    pile_tmp2 = deque()

    while pile :
        pile_tmp.append(pile.pop())
    while pile_tmp :
        pile_tmp2.append(pile_tmp.pop())
    while pile_tmp2 :
        pile.append(pile_tmp2.pop())


#File
from collections import deque

# Création d'une file vide
file = deque()

# Teste si une pile est vide
len(file) == 0

# Ajoute l'élément Truc dans la file
file.append("Truc")

# Suppression (et renvoi) du premier élément inséré dans la file
sommet = pile.popleft()


def copy_file(file):
    file_tmp = deque()
    file_copy = deque()
    while file :
        file_tmp.append(file.popleft())

    while file_tmp :
        el= file_tmp.popleft()
        file.append(el)
        file_copy.append(el)
    return file_copy


def longueur(file) -> int :
    file_tmp = deque()
    l = 0
    while file :
        file_tmp.append(file.popleft())
        l = l+1
    while file_tmp :
        file.append(file_tmp.popleft())
    return l