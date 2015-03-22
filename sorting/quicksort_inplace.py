"""
Quicksort inplace implementation.
"""


def quicksort(items, lo=0, hi=None):
    if hi is None:
        hi = len(items) - 1

    if lo >= hi or len(items) <= 1:
        return

    i = lo
    # simple partitioning (does not handle duplicates well)
    for j in xrange(i, hi):
        if items[j] < items[hi]:
            items[i], items[j] = items[j], items[i]
            i += 1

    # put pivot into the proper place
    items[hi], items[i] = items[i], items[hi]
    print u' '.join(map(str, items))
    quicksort(items, lo, i - 1)
    quicksort(items, i + 1, hi)


if __name__ == '__main__':
    import sys
    _ = sys.stdin.readline()
    items = map(int, sys.stdin.readline().split(' '))
    quicksort(items)