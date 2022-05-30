from pyvis.network import Network
from collections import deque

NonParcouru = "#e0f3db"
AParcourir = "#a8ddb5"
Parcouru = "#43a2ca"
import networkx as nx

sommets = [chr(ord('A')+n) for n in range(6)]

G = Network(height='600px', width='800px',
            directed=True)
net = nx.MultiDiGraph()
net.add_nodes_from(sommets)
net.add_edges_from([    ('A','B'), ('B','A'), ('A','C'), ('F','A'),
                        ('C','B'), ('B','E'), ('C','D'), ('D','C'),
                        ('F','C'), ('D','E'), ('F','D')])
layout = nx.planar_layout(net)

G.from_nx(net)
for node in G.nodes:
    node["x"] = layout[node["id"]][0] * 100
    node["y"] = layout[node["id"]][1] * 100
G.set_edge_smooth('dynamic')
G.toggle_physics(True)
G.set_options("""
var options = {
  "nodes": {
    "font": {
      "size": 36,
      "face": "LM Roman 10"
    }
  }
}
""")



for sommet in sommets:
    G.get_node(sommet)['color'] = NonParcouru

i = 0

# G.repulsion()
# G.show_buttons(filter_=['physics'])
G.save_graph("parcoursProfondeur" + str(i) + ".html")

for racine in sommets:
    if G.get_node(racine)['color'] == NonParcouru:
        pile = deque()
        pile.append(racine)
        G.get_node(racine)['color'] = AParcourir
        i += 1
        G.save_graph("parcoursProfondeur" + str(i) + ".html")
        while pile:
            print(pile)
            sommetActif = pile[-1]
            existeSucceseur = False
            for sommet in G.get_adj_list()[sommetActif]:
                if G.get_node(sommet)['color'] == NonParcouru:
                    existeSucceseur = True
                    pile.append(sommet)
                    G.get_node(sommet)['color'] = AParcourir
                    i += 1
                    G.save_graph("parcoursProfondeur" + str(i) + ".html")
                    break
            if not existeSucceseur:
                G.get_node(sommetActif)['color'] = Parcouru
                pile.pop()
                i += 1
                G.save_graph("parcoursProfondeur" + str(i) + ".html")
