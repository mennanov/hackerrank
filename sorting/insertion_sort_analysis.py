"""
Insertion Sort is a simple sorting technique which was covered in previous challenges.
Sometimes, arrays may be too large for us to wait around for insertion sort to finish.
Is there some other way we can calculate the number of times Insertion Sort shifts each elements when sorting an array?

If ki is the number of elements over which the ith element of the array has to shift, then the total number of shifts
will be k1 +k2 +...+kN.
This problem reduces to counting the number of inversions in the initial array. This can be easily done using
mergesort.
"""


def count_inversions(items, lo=0, hi=None, aux=None):
    if hi is None:
        hi = len(items) - 1

    if lo >= hi:
        return 0

    if aux is None:
        aux = items[:]

    mid = lo + (hi - lo) / 2
    inversions = 0
    il = count_inversions(items, lo, mid, aux)
    ir = count_inversions(items, mid + 1, hi, aux)
    inversions += il + ir
    # merge
    aux[lo:hi + 1] = items[lo:hi + 1]
    i, j = lo, mid + 1
    k = i
    while i <= mid or j <= hi:
        if i > mid:
            items[k] = aux[j]
            j += 1
        elif j > hi:
            items[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            items[k] = aux[i]
            i += 1
        else:
            # that's the inversion: right element is smaller than the left one and all consecutive left items
            inversions += mid - i + 1
            items[k] = aux[j]
            j += 1
        k += 1
    return inversions


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        sys.stdin.readline()
        items = map(int, sys.stdin.readline().strip().split(' '))
        print count_inversions(items)
