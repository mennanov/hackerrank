"""
A series is defined in the following manner:

Given the nth and (n+1)th terms, the (n+2)th can be computed by the following relation
Tn+2 = (Tn+1)^2 + Tn

So, if the first two terms of the series are 0 and 1:
the third term = 1^2 + 0 = 1
fourth term = 1^2 + 1 = 2
fifth term = 2^2 + 1 = 5
... And so on.

Given three integers A, B and N, such that the first two terms of the series (1st and 2nd terms) are A and B
respectively, compute the Nth term of the series.
"""


def fibonacci_modified(a, b, n):
    for i in xrange(n - 2):
        b, a = b ** 2 + a, b
    return b


if __name__ == '__main__':
    import sys

    a, b, n = map(int, sys.stdin.readline().strip().split(' '))
    print fibonacci_modified(a, b, n)