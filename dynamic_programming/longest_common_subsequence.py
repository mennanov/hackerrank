"""
A subsequence is a sequence that can be derived from another sequence by deleting some elements without
changing the order of the remaining elements.
Longest common subsequence (LCS) of 2 sequences is a subsequence,
with maximal length, which is common to both the sequences.

Given two sequence of integers, A=[a1,a2,...,an] and B=[b1,b2,...,bm], find any one longest common subsequence.
"""


def memoize(func):
    cache = dict()

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def lcs(a, b, i=None, j=None):
    if i is None:
        i = len(a) - 1
    if j is None:
        j = len(b) - 1

    if i < 0 or j < 0:
        return []

    if a[i] == b[j]:
        return lcs(a, b, i - 1, j - 1) + [a[i]]
    else:
        return max(lcs(a, b, i - 1, j), lcs(a, b, i, j - 1), key=len)


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    a = tuple(sys.stdin.readline().strip().split(' '))
    b = tuple(sys.stdin.readline().strip().split(' '))
    print ' '.join(lcs(a, b))