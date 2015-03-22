"""
Given two integers, L and R, find the maximal values of A xor B, where A and B satisfy the following condition:

L <= A <= B <= R
"""


def max_xor(lo, hi):
    """
    Straight forward solution. Quadratic time.
    """
    result = float('-inf')
    for i in xrange(lo, hi + 1):
        for j in xrange(i, hi + 1):
            if i ^ j > result:
                result = i ^ j
    return result


def max_xor_bitwise(lo, hi):
    """
    See the comment: https://www.hackerrank.com/challenges/maximizing-xor/forum/comments/42463
    Lets say L = 11011 and R = 11101.
    The trick is to notice that if we xor all pairs in between 11011 and 11101 the highest we can achieve is 00111.
    Notice that 11011 ^ 11101 = 00110.
    There is no way we can turn the first two digits into 1 in the given range,
    because all numbers between 11011 and 11101 will be in the form 11---.
    So XORs between them will always be in the form 00--- and one of them will have to be 00111.
    I am finding 2^3 - 1 = 7 = 111.
    Your answer will always be in the form 2^n - 1. (n=number of digits that we can turn into 1s).
    Complexity is O(1)
    """
    return 2 ** (lo ^ hi).bit_length() - 1


if __name__ == '__main__':
    import sys
    l = int(sys.stdin.readline().strip())
    r = int(sys.stdin.readline().strip())
    print max_xor_bitwise(l, r)