# !/usr/bin/env python
"""Create graph representations from files etc."""
import csv
import scipy as sp
from scipy import sparse


def gettwittergraph():
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

    asd = "asdfasdasd"

    MAXINDEX = 1e7

    A = sparse.dok_matrix((int(MAXINDEX), int(MAXINDEX)))
    indegree = dict()
    outdegree = dict()

    for entry in reader:
        src = int(entry[0])
        dst = int(entry[1])
        if src > MAXINDEX or dst > MAXINDEX:
            continue
        A[dst, src] = 1
        try:
            indegree[dst] += 1
        except KeyError:
            indegree[dst] = 1

        try:
            outdegree[src] += 1
        except KeyError:
            indegree[src] = 1

    return A, dict, dict
