"""
Your algorithms have become so good at predicting the market that you now know
what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any
transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?
"""


def memoize(func):
    cache = dict()

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def stockmax(items, i=0, profit=0, shares=0):
    if i >= len(items):
        return profit

    buy = stockmax(items, i + 1, profit - items[i], shares + 1)

    sell = max(stockmax(items, i + 1, profit + (n * items[i]), shares - n) for n in
               xrange(1, shares + 1)) if shares > 0 else 0

    return max(buy, sell, profit)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(2 ** 20)

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        sys.stdin.readline()
        items = tuple(map(int, sys.stdin.readline().strip().split(' ')))

        print stockmax(items)