import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = {1: 'Dublin', 2: 'Paris', 3: 'Milan', 4: 'Rome', 5: 'Naples', 6: 'Moscow', 7: 'Seoul'}

G.add_nodes_from(nodes.keys())
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 5)])

global_effi = nx.global_efficiency(G)   # 대역효율성
avg_effi = nx.local_efficiency(G)       # 평균대역효율성

print(global_effi)
print(avg_effi)