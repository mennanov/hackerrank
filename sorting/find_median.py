"""
Given a list of numbers, can you find the median in linear time?

Yes, we can. Using a partition routine from the Quicksort algorithm.
"""


def select(items, k, lo=0, hi=None):
    if hi is None:
        hi = len(items) - 1
    if lo >= hi:
        return items[lo]
    # 3-way partitioning
    pivot = items[lo]
    lt = lo
    gt = hi
    i = lo
    while i <= gt:
        if items[i] < pivot:
            items[i], items[lt] = items[lt], items[i]
            lt += 1
            i += 1
        elif items[i] > pivot:
            items[i], items[gt] = items[gt], items[i]
            gt -= 1
        else:
            i += 1
    # lt points to the left-most pivot element, gt points to the right-most pivot element (assuming there are dups)
    if k < lt:
        return select(items, k, lo, lt - 1)
    elif k > gt:
        return select(items, k, gt + 1, hi)
    else:
        return items[k]


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    items = map(int, sys.stdin.readline().strip().split(' '))
    print select(items, len(items) / 2)