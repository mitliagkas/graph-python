import graph
import numpy as np

MAXVALUE = 1e7


def pagerank(a):
    x = np.ones((MAXVALUE, 1))
    alpha = 0.85

    for i in range(4):
        x = a.dot(x)
        x /= np.linalg.norm(x, ord=1)
        x = alpha * x + (1 - alpha) * np.ones((MAXVALUE, 1)) / MAXVALUE

    return x

A, indegree, outdegree = graph.get_twitter_graph()

print A.nnz

# Ac=A.tocsc()
Ar = A.tocsr()

x = pagerank(Ar)

print x.T
ind = np.argmax(x)
print "Maximum of", x[ind], "at position", ind

