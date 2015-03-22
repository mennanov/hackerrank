"""
Given a list of unsorted integers, A={a1,a2,...,aN}, can you find the pair of elements that have
the smallest absolute difference between them?
If there are multiple pairs, find them all.
"""
from collections import defaultdict


def closest_numbers(items):
    if len(items) < 2:
        return
    # sort items (we can do it in linear time using counting sort)
    items.sort()
    diffs = defaultdict(list)
    for i in xrange(1, len(items)):
        diffs[items[i] - items[i - 1]].append((items[i - 1], items[i]))
    # find the smallest diff
    smallest_diff = min(diffs.iterkeys())
    output = []
    for n1, n2 in diffs[smallest_diff]:
        output.append(' '.join((str(n1), str(n2))))
    print ' '.join(output)


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    items = map(int, sys.stdin.readline().strip().split(' '))
    closest_numbers(items)