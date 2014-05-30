import graph
import numpy as np

MAXVALUE=1e7

def pagerank(a):
    x=np.ones((MAXVALUE,1))
    alpha=0.85
    for i in range(4):
        x/=np.linalg.norm(x)
        x=alpha*x+(1-alpha)*np.ones((MAXVALUE,1))

    return x


if __name__ == '__main__':

    A,indegree,outdegree=graph.gettwittergraph()

    print A.nnz

    #Ac=A.tocsc()
    Ar=A.tocsr()

    x=pagerank(Ar)

    print x.T
    print max(x)

