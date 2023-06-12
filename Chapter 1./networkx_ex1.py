import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.layout import bipartite_layout

def draw_graph(G, nodes_position, weight) :
    nx.draw(G, pos = nodes_position, with_labels = True, font_size = 15, node_size = 400, edge_color = 'gray')#, arrowsize = 30)
    
    if weight :
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, nodes_position, edge_labels = edge_labels)

G = nx.Graph()
V = {'Dublin', 'Paris', 'Milan', 'Rome'}
E = [('Paris', 'Dublin', 11), ('Paris', 'Milan', 8), ('Milan', 'Rome', 5), ('Milan', 'Dublin', 19)]

G.add_nodes_from(V)
G.add_weighted_edges_from(E)

nodes_position = nx.circular_layout(G)                              # 노드 위치 자동 계산
#{"Paris": [0,0], "Dublin": [0,1], "Milan": [1,0], "Rome": [1,1]}   # 노드 위치 수동 설정
draw_graph(G, nodes_position, True)