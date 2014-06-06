# !/usr/bin/env python
"""Create graph representations from files etc."""
import csv
from scipy import sparse, stats


def get_twitter_graph():
    """
        Reads the edge list from the twitter file
        http://snap.stanford.edu/data/egonets-Twitter.html
        and creates a sparse directed edge matrix, A.

        eg. if the file contains an line "a b" (a follows b),
        then A[b,a]==1,
        ow A[b,a]==0
    :returns : A scipy sparse matrix (dok) containing all edges.
    :rtype : scipy.sparse.dok_matrix, dict, dict
    """
    filename = '/var/datasets/twitter/twitter_combined.txt'
    reader = csv.reader(open(filename), delimiter=' ')

    MAX_INDEX = 1e7

    A = sparse.dok_matrix((int(MAX_INDEX), int(MAX_INDEX)))
    in_degree = dict()
    out_degree = dict()

    for entry in reader:
        src = int(entry[0])
        dst = int(entry[1])
        if src > MAX_INDEX or dst > MAX_INDEX:
            continue
        A[dst, src] = 1
        try:
            in_degree[dst] += 1
        except KeyError:
            in_degree[dst] = 1

        try:
            out_degree[src] += 1
        except KeyError:
            in_degree[src] = 1

    return A, in_degree, out_degree

def algorithm_one(a):

    alpha=0.1

    n = a.shape[0]

    rvs=stats.bernoulli.rvs(n**(alpha-1), size=n)

    for n in range(n):
        if rvs(n)==1:
            with a[:,n].iterkeys() as out_neighbour:
                counter+=1
                degree_sum+=a[out_neighbour,n]

    return degree_sum, counter







