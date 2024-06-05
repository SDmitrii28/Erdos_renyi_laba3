import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 16 
p = 0.45 

G = nx.erdos_renyi_graph(n, p)

degrees = [degree for node, degree in G.degree()]
average_degree_computed = np.mean(degrees)

average_degree_theoretical = p * (n - 1)

print(f"Средняя степень вершины (вычисленная): {average_degree_computed:.4f}")
print(f"Средняя степень вершины (теоретическая): {average_degree_theoretical:.4f}")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
plt.title(f"Граф Эрдёша-Реньи (n={n}, p={p})")
plt.show()
