import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
V = {'Dublin', 'Paris', 'Milan', 'Rome'}
E = [('Milan', 'Dublin'), ('Milan', 'Paris'), ('Paris', 'Dublin'), ('Milan', 'Rome')]

G.add_nodes_from(V)
G.add_edges_from(E)

print(f"V = {G.nodes}") # 노드
print(f"E = {G.edges}") # 간선

print(f"Graph Order : {G.number_of_nodes()}")                                   # 위수
print(f"Graph Size : {G.number_of_edges()}")                                    # 크기
print(f"Degree for nodes : {{v : G.degree(v) for v in G.nodes}}")               # 차수
print(f"Neigjbors for nodes : {{v : list(G.neighbors(v)) for v in G.nodes}}")   # 근방노드

ego_graph_milan = nx.ego_graph(G, "Milan")  # 특정 노드의 에고그래프
print(f"Nodes : {ego_graph_milan.nodes}")
print(f"Edges : {ego_graph_milan.edges}")

new_nodes = {'London', 'Madrid'}
new_edges = [('London', 'Rome'), ('Madrid', 'Paris')]
G.add_nodes_from(new_nodes) # 새로운 노드 추가
G.add_edges_from(new_edges) # 새로운 간선 추가
print(f"V = {G.nodes}")
print(f"V = {G.edges}")

# 노드 삭제
G.remove_nodes_from(new_nodes)  
print(f"V = {G.nodes}")
print(f"V = {G.edges}")

node_edges = [('Milan', 'Dublin'), ('Milan', 'Paris')]
G.remove_edges_from(node_edges) 
print(f"V = {G.nodes}")
print(f"V = {G.edges}")