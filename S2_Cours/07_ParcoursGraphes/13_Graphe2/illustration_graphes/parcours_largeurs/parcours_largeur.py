from pyvis.network import Network
from collections import deque

NonParcouru = "#e0f3db"
AParcourir = "#a8ddb5"
Parcouru = "#43a2ca"
import networkx as nx

sommets = [chr(n) for n in range(ord('A'), ord('A') + 7)]

G = Network(height='600px', width='800px',
            directed=True)
net = nx.nx.MultiDiGraph()
net.add_nodes_from(sommets)
net.add_edges_from([    ('A','B'), ('B','A'), ('A','C'), ('G','A'),
                        ('B','C'), ('B','E'), ('C','E'), ('C','G'),
                        ('D','C'), ('F','C'), ('D','E'), ('D','F')])
layout = nx.planar_layout(net)

G.from_nx(net)
for node in G.nodes:
    node["x"] = layout[node["id"]][0] * 200
    node["y"] = layout[node["id"]][1] * 200
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
# G.show_buttons()
# G.show("parcoursLargeur" + str(i) + ".html")
G.save_graph("parcoursLargeur" + str(i) + ".html")

for racine in sommets:
    if G.get_node(racine)['color'] == NonParcouru:
        file = deque()
        file.append(racine)
        G.get_node(racine)['color'] = AParcourir
        i += 1
        G.save_graph("parcoursLargeur" + str(i) + ".html")
        while file:
            sommetActif = file.popleft()
            for sommet in G.get_adj_list()[sommetActif]:
                if G.get_node(sommet)['color'] == NonParcouru:
                    file.append(sommet)
                    G.get_node(sommet)['color'] = AParcourir
            G.get_node(sommetActif)['color'] = Parcouru
            i += 1
            G.save_graph("parcoursLargeur" + str(i) + ".html")
