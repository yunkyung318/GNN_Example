import networkx as nx
from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder
import matplotlib.pyplot as plt

G = nx.barbell_graph(m1 =7, m2 = 4)
node2vec = Node2Vec(G, dimensions = 2)
model = node2vec.fit(window = 10)

edges_embs = HadamardEmbedder(keyed_vectors=model.wv)
fig, ax = plt.subplots()
for x in G.nodes() :
    v = model.wv.get_vector(str(x))
    ax.scatter(v[0], v[1], s = 1000)
    ax.annotate(str(x), (v[0], v[1]), fontsize =12)