import networkx as nx
import numpy as np
import pandas as pd
import numpy as np
from networkx.drawing.layout import bipartite_layout

n_nodes = 10
n_edges = 12

bottoms_nodes = [ith for ith in range(n_nodes) if ith % 2 == 0]
top_nodes = [ith for ith in range(n_nodes) if ith % 2 == 1]

iter_edges = zip(np.random.choice(bottoms_nodes, n_edges), np.random.choice(top_nodes, n_edges))
edges = pd.DataFrame([{"source": a, "target": b} for a, b in iter_edges])

B = nx.Graph()
B.add_nodes_from(bottoms_nodes, bipartite = 0)      # bipartite 변수로 노드 집합 구분
B.add_nodes_from(top_nodes, bipartite = 1)
B.add_nodes_from([tuple(x) for x in edges.values])

pos = bipartite_layout(B, bottoms_nodes)            # 노드를 두 개의 직선으로 배치
nx.draw_networkx(B, pos=pos)