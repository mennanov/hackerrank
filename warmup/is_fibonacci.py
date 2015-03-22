"""
You are given an integer, N. Write a program to determine if N is an element of the Fibonacci sequence.

Rather than compute all fibonacci numbers below N, we will use the fact:
A number, n, is a Fibonacci number if and only if (5n^2 + 4) or (5n^2 - 4) is a perfect square.
"""
import math


def is_fibonacci(n):
    s1 = 5 * (n ** 2) - 4
    s2 = 5 * (n ** 2) + 4
    return math.sqrt(s1) == int(math.sqrt(s1)) or math.sqrt(s2) == int(math.sqrt(s2))


if __name__ == '__main__':
    import sys

    _ = int(sys.stdin.readline())
    for n in sys.stdin.readlines():
        print 'IsFibo' if is_fibonacci(int(n)) else 'IsNotFibo'