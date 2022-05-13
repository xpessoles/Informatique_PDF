import matplotlib.pyplot as plt
import networkx as nx

G=[[0,1,1,0,1,1,1,0],[1,0,1,0,0,0,0,1],[1,1,0,1,1,0,0,1],[0,0,1,0,1,0,0,0],[1,0,1,1,0,1,0,0],[1,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,1],[0,1,1,0,0,0,1,0]]

# La matrice est symétrique donc personne a menti

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
    # Gx.add_node(0,label='A',col='pink')
    # Gx.add_node(1,label='B',col='red')
    # Gx.add_node(2,label='C',col='white')
    # Gx.add_node(3,label='D',col='white')
    # Gx.add_node(4,label='E',col='white')
    # Gx.add_node(5,label='F',col='blue')
    # Gx.add_node(6,label='G',col='blue')
    # Gx.add_node(7,label='H',col='blue')
    # liste = list(Gx.nodes(data='label'))
    # labels_nodes = {}
    # for noeud in liste:
    #     labels_nodes[noeud[0]]=noeud[1]
    edges=aretes(G)
    Gx.add_edges_from(edges)
    # pos = nx.spring_layout(Gx)
    # nx.draw_networkx_nodes(Gx, pos, node_size=700,alpha=0.9)
    # nx.draw_networkx_labels(Gx, pos, labels=labels_nodes, with_labels=True, font_size=20, font_color='black',font_family='sans-serif')
    nx.draw(Gx,with_labels = True)
    plt.show()


plt.figure('graphe meurtre')
plot_graphe(G)