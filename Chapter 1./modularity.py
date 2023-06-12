import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_com

G = nx.Graph()
nodes = {1: 'Dublin', 2: 'Paris', 3: 'Milan', 4: 'Rome', 5: 'Naples', 6: 'Moscow', 7: 'Seoul'}

G.add_nodes_from(nodes.keys())
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 5)])

modular = nx_com.modularity(G, communities=[{1, 2, 3}, {4, 5, 6, 7}])   # 모듈성, communities == 그래프의 분할
print(modular)