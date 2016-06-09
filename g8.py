import matplotlib.pyplot as plt
import networkx as nx

nodes = [(0, 0), (0, 1),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

G = nx.Graph()

G.add_nodes_from(nodes)

for i in range(3):
    G.add_edge((0, 0), (1, i))
    G.add_edge((0, 1), (1, i))

    G.add_edge((1, i), (2, i))

G.add_edge((2, 0), (2, 1))
G.add_edge((2, 1), (2, 2))
G.add_edge((2, 2), (2, 0))

print(len(G), max(G.degree().values()), nx.diameter(G))

nx.draw_networkx(G)
plt.show()
