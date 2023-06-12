import networkx as nx
import matplotlib.pyplot as plt

directed_multi_graph = nx.MultiDiGraph()        # 유향다중그래프
undirected_multi_graph = nx.MultiGraph()        # 무향다중그래프

V = {'Dublin', 'Paris', 'Milan', 'Rome'}
E = [('Milan', 'Dublin'), ('Milan', 'Dublin'), ('Paris', 'Milan'), ('Paris', 'Dublin'), ('Milan', 'Rome'), ('Milan', 'Rome')]

directed_multi_graph.add_nodes_from(V)
undirected_multi_graph.add_nodes_from(V)

directed_multi_graph.add_edges_from(E)
undirected_multi_graph.add_edges_from(E)