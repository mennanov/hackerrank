"""
You are given a tree (a simple connected graph with no cycles).
You have to remove as many edges from the tree as possible to obtain a forest with the condition that:
Each connected component of the forest should contain an even number of vertices.

To accomplish this, you will remove some edges from the tree. Find out the number of removed edges.
"""
from collections import defaultdict


def even_tree(vertices):
    rank = dict()
    removed = set()

    def height(v, f=None):
        if (v, f) not in rank:
            r = 1
            for u in vertices[v]:
                if (f is None or u != f) and (u, v) not in removed:
                    r += height(u, v)
            rank[(v, f)] = r
        return rank[(v, f)]

    for v, adj in vertices.iteritems():
        for u in adj:
            # if it is an even subtree - remove this edge
            if (u, v) not in removed and height(u, v) % 2 == 0:
                removed.add((v, u))
                removed.add((u, v))
    return len(removed) / 2


if __name__ == '__main__':
    import sys

    vertices = defaultdict(set)
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    for _ in xrange(m):
        u, v = map(int, sys.stdin.readline().strip().split(' '))
        # add edge from u to v
        vertices[u].add(v)
        # add edge from v to u
        vertices[v].add(u)
    print even_tree(vertices)