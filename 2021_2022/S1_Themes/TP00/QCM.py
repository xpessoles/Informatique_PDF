# QCM

# Variables et types de variables

# Question 1

a = 5
a = a+3
print(a)


# Je ne sais pas.
# 3
# 5
# 8
# a


# Question 2
a = 3
b = 4
a = b
print(a)


# Je ne sais pas.
# 3
# 4
# b
# a



# Question 3
# Quel est le type de a
a = "64"



print(type(a))
# Bool
# Integer
# Float
# String




# Question 4
# Quel est le type de a
a = 64
print(type(a))
# Bool
# Integer
# Float
# String

# Question 5
a = "Sa"
b = "lut"
print(b+a)

# b + a
# B 	Salut
# C 	lutSa
# D 	Erreur

# Question 6
# Quel est le résultat de l'instruction suivante :
16%4

# Je ne sais pas
# 16
# 4
# 0
# 1



# Question 7
# Quel est le résultat de l'instruction suivante :
0 == 0

# 0
# 1
# True
# False
# Je ne sais pas

# Question 8
# Quel est le résultat de l'instruction suivante :
0 != 0

# 0
# 1
# True
# False
# Je ne sais pas




# Question 9
# Quel est le résultat du script suivant :
L = [1,2,3]
print(len(L))

# 0
# 1
# 2
# 3

# Question 10
# Quel est le résultat du script suivant :
L = [1,2,3]
print(L[1])

# 0
# 1
# 2
# 3

# Question 11
# Quel est le résultat du script suivant :
L = [1,2,3]
L.append(4)
print(L)

# [1,2,3,4]
# [4,1,2,3]
# [1,2,3]
# [1,2,34]
# Je ne sais pas


# Question 12
# Quel est le résultat du script suivant
jour=1
while (jour<7) :
    jour = jour+1
    print(jour)

# 1234567 (sur des lignes séparées)
# 123456
# 23456
# 234567
# 6

# Question 13
# Quel est le résultat du script suivant :
jour = 2
while (jour<7):
    jour = jour +1
print(jour)

# 1
# 6
# 7
# 23456


# Question 14
age = 16
if (age>=18):
    print("Majeur")

# A 	Majeur
# B 	Rien
# C 	ERROR
# D 	Mineur


# Question 15
# Quel est le résultat du script suivant :
age = 16
if (age>=18):
    print("Majeur")
print("Monsieur")

# A 	Rien
# B 	Majeur
# Monsieur
#
# C 	ERROR
# D 	Monsieur



# Question 16
# Quel est le résultat du script suivant :
a = 8
b = 12
if (a>5) :
    b = b-5
if (b>10) :
    b = b+3
print(b)

# A 	7
# B 	10
# C 	12
# D 	15


# Question 17
a=3
b=6
if (a>5) and (b!=10):
    b=4
else :
    b=2
print(b)

# A 	2
# B 	4
# C 	6
# D 	ERROR

# Question 18
def bonjour(nb):
    return nb+3

print(bonjour(5))

# A 	Erreur
# B 	5
# C 	8
# D 	3

# Question 19
def bonjour():
    a = 1
    print(a)
a=10
bonjour()


# A 	bonjour
# B 	11
# C 	1
# D 	10


# Question 20

def func(a):
    a += 2.0
    return a

a = func(8.0)
print(a)
 # Je ne sais pas
 # A) 8.0
 # B) 10.0
 # C) 12.0
 # a




# Question 21
def f(t):
    n = len(t)
    for k in range(1,n):
        t[k] = t[k] + 1

L = [1, 3, 4, 5, 2]
f(L)



