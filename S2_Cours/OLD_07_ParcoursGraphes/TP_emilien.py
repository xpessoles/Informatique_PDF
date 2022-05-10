import numpy as np
import matplotlib.pyplot as plt

#Q1
G=-1*np.ones([5,5])+np.eye((5))

G[0,1],G[1,0]=9,9
G[0,2],G[2,0]=3,3
G[0,4],G[4,0]=7,7
G[1,2],G[2,1]=1,1
G[1,3],G[3,1]=8,8
G[2,3],G[3,2]=4,4
G[2,4],G[4,2]=2,2


#Q2
def voisins(G:list,i:int):
    L=[]
    for j in range(len(G[i][:])):
        if G[i][j]!=-1 and G[i,j]!=0:
            L.append(j)
    return L


#Q3
def arretes(G:list):
    L=[]
    for i in range(len(G)):
        for j in range(i):
            if G[i][j]!=-1:
                L.append((i,j))
    return L

#Q4
import networkx as nx
def plot_graphe(G,nom):
    plt.clf()
    Gx = nx.Graph()
    edges = arretes(G)
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    #plt.show()
    plt.savefig(nom)

plot_graphe(G,'graphe0.png')

#Q5
def degre(G:list, i:int):
    return len(voisins(G,i))


#Q6
def longueur(G:list,L:list):
    i=L[0]
    s=0
    for j in L[1:]:
        if j in voisins(G,i):
            s+=G[i][j]
            i=j
        else:
            return -1
    return s

def conv_liste(G):
    NG=[]
    for ligne in G:
        NG.append(list(ligne))
    return NG


#Q7
L=[0,2,4]
poids=[7,8,9]


G=conv_liste(G)

def ajout_sommet(G:list, L:list, poids : list):
    col=[]
    for i in range(len(G)):
        if i in L:
            x=poids[L.index(i)]
        else:
            x=-1
        G[i].append(x)
        col.append(x)
    col.append(0)
    G.append(col)

#ajout_sommet(G,L,poids)
#plot_graphe(G,'graphe1.png')

#Q8
def supprime_sommet(G:list, i: int):
    G.pop(i)
    for k in range(len(G)):
        G[k].pop(i)


#Q9
G2=[[1,2,4],[0,2,3],[0,1,3,4],[1,2],[0,2]]

#Q10
def voisins_l(G,i):
    return G[i]

#Q11
def arretes_l(G):
    L=[]
    for i in range(len(G)):
        for j in range(len(G[i])):
            if (G[i][j],i) not in L:
                L.append((i,G[i][j]))
    return L

#Q12

def plot_graphe_l(G,nom):
    plt.clf()
    Gx = nx.Graph()
    edges = arretes_l(G)
    Gx.add_edges_from(edges)
    nx.draw(Gx,with_labels = True)
    plt.savefig(nom)
    #plt.show()

plot_graphe_l(G2,'graphe2.png')

#Q13
def degre_l(G,i):
    return len(G[i])


#Q14
def ajout_sommet_l(G:list, L:list):
    for i in L:
        G[i].append(len(G))
    G.append(L)

#Q15
def supprime_sommet_l(G:list, i:int):
    for k in range(len(G)):
        if i in G[k]:
            G[k].pop(G[k].index(i))
    G.pop(i)




