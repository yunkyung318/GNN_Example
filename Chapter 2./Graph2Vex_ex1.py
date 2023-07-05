import random
import matplotlib.pyplot as plt
from karateclub import Graph2Vec
n_graphs = 20

def generate_random() :
    n = random.randint(5, 20)
    k = random.randint(5, n)
    p = random.uniform(0, 1)
    return nx.watts_strogatz_graph(n, k, p)

Gs = [generate_random() for x in range(n_graphs)]
model = Graph2Vec(dimensions=2)
model.fit(Gs)
embeddings = model.get_embedding()

fig, ax = plt.subplots(figsize=(10, 10))
for i, vec in enumerate(embeddings) :
    ax.scatter(vec[0], vec[1], s = 1000)
    ax.annotate(str(i), (vec[0], vec[1]), fontsize = 16)