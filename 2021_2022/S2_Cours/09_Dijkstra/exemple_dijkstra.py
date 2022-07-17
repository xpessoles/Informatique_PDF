from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

G1 = {"s":["1","4"],
      "t":["0","2","5","6"],
      "y":["3","6"],
      "x":["2","7"],
      "z":["5"]}

 #Matrice adjacence successeur
G=[[0,9,-1,5,-1],[-1,0,1,2,-1],[-1,-1,0,-1,4],[-1,3,9,0,2],[7,-1,6,-1,0]]

G=[[0,9,10000,5,10000],[10000,0,1,2,10000],[10000,10000,0,10000,4],[10000,3,9,0,2],[7,10000,6,10000,0]]

#Matrice adjacence prédécesseur
# G=[[0,-1,-1,-1,7],[9,0,-1,3,-1],[-1,1,0,9,6],[5,2,-1,0,-1],[-1,-1,4,2,0]]
#
# G=[[0,10000,10000,10000,7],[9,0,10000,3,10000],[10000,1,0,9,6],[5,2,10000,0,10000],[10000,10000,4,2,0]]

def aretes(G:list)->list:
    L=[]
    for i in range(len(G)):
        for j in range(len(G)):
            if not G[i][j]==0:
                L.append((i,j))
    return L

def plot_graphe(G):
    Gx=nx.DiGraph()
    edges=aretes(G)
    Gx.add_edges_from(edges)

    nx.draw(Gx,with_labels = True)
    plt.show()

#plot_graphe(G)

def cherche_min(d, traites):
    """ Renvoie le sommet i vérifiant d[i] minimal et traites[i] faux, s'il existe un tel .
    sommet
    tel que d[i] != inf. Sinon, renvoie -1 """
    n=len(d)
    x=-1
    for i in range(n):
        if not traites[i] and d[i] != float('inf') and (x==-1 or d[x]>d[i]):
            x=i
    return x


def dijkstra_mat(G,s):
    """
    G donné par matrice d'adjacence. Renvoie les poids chemins de plus petits poids depuis s.
    """
    n=len(G)
    d = [float('inf')]*n
    d[s]=0
    traites = [False]*n
    while True:
        x=cherche_min(d,traites)
        print(x,d,traites)
        if x==-1:
            return d
        for i in range(n):
            d[i]=min(d[i], d[x]+G[x][i])
        traites[x]=True
    return d