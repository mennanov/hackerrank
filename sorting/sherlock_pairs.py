"""
Sherlock is given an array of N integers by Watson.
Now Watson asks Sherlock how many different pairs of indices i and j exist such
that i is not equal to j but Ai is equal to Aj.

That is, Sherlock has to count the total number of pairs of indices (i,j) where Ai = Aj AND i != j.
Example: 1 1 2 will make 2 pairs: 0, 1 and 1, 0
"""
from collections import Counter


choose = lambda n: n * (n - 1)


def count_pairs(items):
    """
    O(N) time and O(N) space solution.
    We may use binary search and sorting to get O(NlogN) time and O(1) space.
    """
    counter = Counter(items)
    pairs = 0
    for n, v in counter.iteritems():
        if v > 1:
            pairs += choose(v)
    return pairs


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        sys.stdin.readline()
        items = map(int, sys.stdin.readline().strip().split(' '))
        print count_pairs(items)