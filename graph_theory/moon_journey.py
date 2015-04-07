"""
The member states of the UN are planning to send 2 people to the Moon. But there is a problem.
In line with their principles of global unity, they want to pair astronauts of 2 different countries.

There are N trained astronauts numbered from 0 to N-1. But those in charge of the mission did not receive information
about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts
belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts belonging to different countries.
Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know
their country directly. For instance, if 1,2,3 are astronauts from the same country;
it is sufficient to mention that (1,2) and (2,3) are pairs of astronauts from the same country
without providing information about a third pair (1,3).
"""


class UF(object):
    """
    Union-find data structure with sub-logarithmic operations complexity.
    """

    def __init__(self):
        self.ids = dict()
        self.rank = dict()

    def add(self, elem):
        self.ids[elem] = elem
        self.rank[elem] = 1

    def root(self, elem):
        while self.ids[elem] != elem:
            # parent look-up with path compression
            self.ids[elem] = self.ids[self.ids[elem]]
            elem = self.ids[elem]
        return elem

    def union(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        if a_root != b_root:
            if self.rank[a_root] < self.rank[b_root]:
                # add root of a to the root of b
                self.ids[a_root] = b_root
                self.rank[b_root] += self.rank[a_root]
                del self.rank[a_root]
            else:
                # add root of b to the root of a
                self.ids[b_root] = a_root
                self.rank[a_root] += self.rank[b_root]
                del self.rank[b_root]

    def connected(self, a, b):
        return self.root(a) == self.root(b)


if __name__ == '__main__':
    import sys

    uf = UF()
    n, i = map(int, sys.stdin.readline().strip().split(' '))
    for j in xrange(n):
        uf.add(j)
    for j in xrange(i):
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        uf.union(a, b)

    choose2 = lambda n: n * (n - 1) / 2
    s = choose2(n)
    for group in uf.rank.itervalues():
        s -= choose2(group)
    print s
