###################
#####Remarques#####
###################


#Bien insister sur la syntaxe vue en cours:
#f = open('fichier.csv', 'r')
#les_lignes = f.readlines()
#f.close()
#for ligne in les_lignes:   #éventuellemment les_lignes[n0:]
#   liste = ligne.strip().split(sep)  #sep = '\t' ou sep = ';'

###############
#####exo 1#####
###############
import matplotlib.pyplot as plt



f = open('uhing_info.csv', 'r', encoding = 'utf8')
les_lignes = f.readlines()
f.close()


print (les_lignes[:15])
# ['Date Essai;14/11/2021;;;;;;;;\n', 'Heure Essai;10:21;;;;;;;;\n', 'Frequence (Hz);1000.0;;;;;;;;\n', 'Fonctionnement;Uhing;;;;;;;;\n', 'Type Pilotage;Creneau;;;;;;;;\n', 'Nb cycles;1;;;;;;;;\n', 'Duree de marche (s);5.00;;;;;;;;\n', "Duree d'arret (s);1.00;;;;;;;;\n", 'Vitesse (tr/min);1000.0;;;;;;;;\n', ' ;;;;;;;;;\n', 'Nb points de consigne;2001;;;;;;;;\n', 'dt consigne;0.003;;;;;;;;\n', 'Temps (s);Consigne (tr/min);Vitesse du moteur (tr/min);Vitesse lineaire (mm/s);Courant (A);Angle (deg);Vitesse lineaire calculee (mm/s);Vitesse de glissement (mm/s);Deplacement (mm);Pas (mm)\n', '0.0000;1000.000;0.000;0.000;0.000;5.550;0.000;0.000;0.000;4.579\n', '0.0010;1000.000;2.272;0.013;0.000;5.726;0.179;0.166;0.000;4.726\n']



# print (type(les_lignes))
# <class 'list'>


# print (type(les_lignes[0]))
# <class 'str'>

stockage=[]
for ligne in les_lignes:
    ligne=ligne.strip()
    liste=ligne.split(';')
    stockage.append(liste)

# print (stockage[:15])

# print (stockage[12])
# ['"Temps (s)', 'Consigne (tr/min)', 'Vitesse du moteur (tr/min)', 'Vitesse lineaire (mm/s)', 'Courant (A)', 'Angle (deg)', 'Vitesse lineaire calculee (mm/s)', 'Vitesse de glissement (mm/s)', 'Deplacement (mm)', 'Pas (mm)"']


print (stockage[13:17])
# [['0.0000', '1000.000', '0.000', '0.000', '0.000', '5.550', '0.000', '0.000', '0.000', '4.579'], ['0.0010', '1000.000', '2.272', '0.013', '0.000', '5.726', '0.179', '0.166', '0.000', '4.726'], ['0.0020', '1000.000', '15.511', '0.013', '9.756', '5.726', '1.222', '1.209', '0.000', '4.726'], ['0.0030', '1000.000', '65.453', '0.504', '14.571', '5.726', '5.155', '4.651', '0.001', '4.726']]


### questions 6 et 7
les_temps=[]
consigne=[]
les_vitesses=[]
for donnees in stockage[13:]:
    les_temps.append(float(donnees[0]))
    consigne.append(float(donnees[1]))
    les_vitesses.append(float(donnees[2]))

### question 8
plt.figure('vitesses')
plt.plot(les_temps,consigne,label='consigne')
plt.plot(les_temps,les_vitesses,label='vitesse mesurée')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Mesures de vitesse du Uhing')
plt.legend()
plt.show()

les_temps_permanent=les_temps[1000:5000]
consigne_permanent=consigne[1000:5000]
# vitesses_permanent=les_vitesses[1000:5000]

### question 9 temps entre 0 et 1s
les_temps2=[]
les_vitesses2=[]
i=0
while les_temps[i]<0.6:
    les_temps2.append(les_temps[i])
    les_vitesses2.append(les_vitesses[i])
    i+=1


### question 10
plt.figure('question 10')
plt.plot(les_temps2,les_vitesses2,label='vitesse mesurée')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Mesures de vitesse du Uhing')
plt.legend()
plt.show()

### question 11
def lisser(L:list,n):
    L1=[]
    for i in range(0,len(L)-n):
        L1.append(sum(L[i:i+n])/n)
    return L1+L[-n:]

### question 12
vitesse_lissee=lisser(les_vitesses2,3)


import numpy as np


### question 13
def modele2ordre(z,omega,t,E0):
    return E0*(1-np.exp(-omega*z*t)*(np.cos(omega*np.sqrt(1-z**2)*t)+(z/np.sqrt(1-z**2))*np.sin(omega*np.sqrt(1-z**2)*t)))


### question 14
s=[modele2ordre(0.7,40,t,1000) for t in les_temps2]

### question 15
plt.figure('vitesses modele et essai')
plt.plot(les_temps2,vitesse_lissee,label='lissee')
plt.plot(les_temps2,s,label='vitesse calculée')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Mesures de vitesse du Uhing')
plt.legend()
plt.show()







# >>> max(les_vitesses2)
# 1149.165
#
# >>> max(vitesse_lissee)
# 1109.6722




plt.figure('vitesses 2')
plt.plot(les_temps2,vitesse_lissee,label='lissee')
plt.plot(les_temps2,les_vitesses2,label='vitesse mesurée')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Mesures de vitesse du Uhing')
plt.legend()
plt.show()

### question 16
z=0.7
s=[modele2ordre(z,53,t,1000) for t in les_temps2]
while abs(max(s)-max(les_vitesses2))>1:
    z=z-0.001
    s=[modele2ordre(z,53,t,1000) for t in les_temps2]
# print (z,abs(max(s)-max(vitesse_lissee)))
# 0.5219999999999998 0.9193850984356686

# print (z,abs(max(s)-max(les_vitesses2)))
# 0.5189999999999998 0.7399161285770788


### question 18
plt.figure('vitesses modele')
L_ecart=[]
for omega in [30,35,40,45,50,55,60,65]:
    modele=[modele2ordre(0.5219,omega,t,1000) for t in les_temps2]
    ecart=0
    for i in range(len(modele)):
        ecart+=abs(modele[i]-vitesse_lissee[i])/vitesse_lissee[i]
    L_ecart.append(ecart)
    plt.plot(les_temps2,modele,label='omega ='+str(omega))
plt.plot(les_temps2,vitesse_lissee,label='vitesse lissée')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Mesures de vitesse du Uhing')
plt.legend()
plt.show()

### question 19
plt.figure('histo')
plt.bar([30,35,40,45,50,55,60,65],L_ecart,color='blue',edgecolor='black')
plt.xlabel('omega en rad/s')
plt.ylabel('écart réponse réelle et simulée')
plt.show()
#
# plt.figure()
# plt.hist(les_ecart, bins=15, density=True, range=(-7,8), edgecolor = 'black')
# plt.show()

### question 20
modele=[modele2ordre(0.5219,55,t,1000) for t in les_temps2]

plt.figure('choix')
plt.plot(les_temps2,vitesse_lissee,label='lissee')
plt.plot(les_temps2,modele,label='modèle')
plt.xlabel('temps en seconde')
plt.ylabel('vitesse en tr/min')
plt.title('Comparaison modèle et réel')
plt.legend()
plt.show()

