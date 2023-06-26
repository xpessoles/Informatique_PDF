import random as r
import matplotlib.pyplot as plt
import time
import math as m

### Q1
def recherche_sequentielle(L:list,val:int) -> bool:
    n=len(L)
    i=0
    while i<n and not L[i]==val:
        i=i+1
    return (not i==n,i)


### Q2
def recherche_sequentielle_triee(L:list,val:int) -> bool:
    if val<L[0] or val>L[-1]:
        return False
    n=len(L)
    i=0
    while i<n and not L[i]==val and L[i]<val:
        i=i+1
    return (not i==n,i)

### Q3
L1=[17, 24, 31, 33, 43, 52, 79, 80, 120, 126, 153, 188, 226, 254, 270, 277, 284, 289, 302, 318, 319, 345, 352, 392, 403, 413, 420, 439, 468, 480]
# tests
print (recherche_sequentielle_triee(L1,79))
print (recherche_sequentielle_triee(L1,L1[0]))
print (recherche_sequentielle_triee(L1,L1[-1]))
print (recherche_sequentielle_triee(L1,L1[-1]+3))

### Q4
L=[r.randint(0,10000000) for i in range(10000000)]
L.sort()
val_a_cherchee= L[-1]
temps = time.perf_counter()
test2=val_a_cherchee in L
print('le temps mis par la recherche interne: ',time.perf_counter()-temps,'secondes')
print(test2)
temps = time.perf_counter()
test3=recherche_sequentielle(L,val_a_cherchee)
print('le temps mis par la recherche séquentielle : ',time.perf_counter()-temps,'secondes')
print(test3)

### Q5&7&8
def recherche_dicho(L,val):
    n=len(L)
    g = 0
    d = n-1
    rep=False
    nb_iteration=0
    while g<=d and rep==False :
        m=(g+d)//2
        if L[m] == val:
            rep=True

        elif val<L[m]:
            d=m-1
        else:
            g=m+1

        nb_iteration+=1

    return rep,nb_iteration

# temps = time.perf_counter()
# test4=recherche_dicho(L,val_a_cherchee)
# print('le temps mis par la méthode dicho: ',time.perf_counter()-temps,'secondes')
# print(test4)


### Q6
# # jeu de test pour voir si l'algo fonctionne :
# print(recherche_dicho(L,-2)) #algo marche si la valeur est avant la borne inférieure
# print(recherche_dicho(L,10000000000)) #ou après le max
# print(recherche_dicho(L,L[100])) #valeur présente
# print(recherche_dicho(L,L[100]+1)) #valeur non présente à l'intérieur
# print(recherche_dicho([],1)) #test avec une liste vide



### Q9


Les_temps_seq=[]
Les_temps_dicho=[]

Nmax=100 # longueur max de la liste

for i in range(1,Nmax,5):
    L=[r.randint(0,i) for j in range(i)]
    L.sort()

    td=time.perf_counter()
    recherche_sequentielle(L,L[-1])
    tf=time.perf_counter()
    Les_temps_seq.append(tf-td)

    td=time.perf_counter()
    recherche_dicho(L,i+1)
    tf=time.perf_counter()
    Les_temps_dicho.append(tf-td)


### Q10&11 :

tailles=[i for i in range(1,Nmax,5)]
plt.figure(1)
plt.plot(tailles,Les_temps_seq,label='sequentielle')
plt.plot(tailles,Les_temps_dicho,label='dichotomique')
plt.xlabel('taille de la liste')
plt.ylabel('temps en seconde')
plt.legend()
plt.show()



# ### Q11  avec itérations
# iteration_dicho=[]
# Val=2587
#
# for i in range(100,1000200,50000):
#     L=[(r.randint(0,i))*2 for j in range(i)]
#     L.sort()
#     a=recherche_dicho(L,val)
#     iteration_dicho.append(a[1])
# plt.figure(2)
#
# les_x=[i for i in range(100,1000200,50000)]
# plt.plot(les_x,iteration_dicho,label='itération dichotomique')
# plt.xlabel('taille de la liste')
# plt.ylabel("nombre d'itération")
# plt.legend()
# plt.show()

### Q12
iteration_dicho=[]
les_x=[2**i for i in range(5,24)]

for i in les_x:
    L=[r.randint(0,i) for j in range(i)]
    L.sort()
    b=recherche_dicho(L,L[-1])
    iteration_dicho.append(b[1])

### Q13
plt.figure(3)
les_x=[2**i for i in range(5,24)]
les_y=[m.log2(x) for x in les_x]
plt.plot(les_x,les_y,label='logarithme base 2')
plt.plot(les_x,iteration_dicho,label='itération dichotomique')
plt.xlabel('taille de la liste')
plt.ylabel("nombre d'itération")
plt.legend()
plt.show()

