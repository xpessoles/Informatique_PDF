import matplotlib.pyplot as plt
import networkx as nx

G=[[0,1,1],[1,0,1],[1,0,0]]



for element in G:
    print (element)


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


plt.figure('graphe exemple')
plot_graphe(G)