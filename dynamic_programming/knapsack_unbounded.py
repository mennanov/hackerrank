"""
Given a list of n integers, A={a1,a2,...,an}, and another integer, k representing the expected sum.
Select zero or more numbers from A such that the sum of these numbers is as near as possible, but not exceeding,
to the expected sum (k).

Note:

Each element of A can be selected multiple times.
If no element is selected then the sum is 0.
"""


def memoize(func):
    cache = dict()

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def knapsack(items, k):
    if k <= 0:
        return 0

    highest = 0
    for item in items:
        if item <= k:
            h = knapsack(items, k - item) + item
            if h > highest:
                highest = h
    return highest


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(2 ** 20)

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        n, k = map(int, sys.stdin.readline().strip().split(' '))
        items = tuple(map(int, sys.stdin.readline().strip().split(' ')))
        print knapsack(items, k)