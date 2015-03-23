"""
Given an array with n elements, can you sort this array in ascending order using only one of the following operations?
1. Swap two elements.
2. Reverse one sub-segment.
"""
from operator import gt, lt


def is_sorted(items, lo, hi, op):
    for i in xrange(lo + 1, hi + 1):
        if op(items[i], items[i - 1]):
            return False
    return True


def almost_sorted(items):
    """
    Linear time solution.
    """
    # find the left and right incorrect elements
    left, right = None, None
    n = len(items) - 1
    for i in xrange(n):
        if left is None and items[i] > items[i + 1]:
            left = i
        if right is None and items[n - i] < items[n - i - 1]:
            right = n - i
    if left is None and right is None:
        # already sorted
        print 'yes'
    else:
        # the list before left and after right is sorted, need to look between left and right
        asc = is_sorted(items, left + 1, right - 1, lt)
        desc = is_sorted(items, left + 1, right - 1, gt)
        swap = (items[left] >= items[right - 1] and (right == n or items[left] <= items[right + 1])) and (
            items[right] <= items[left + 1] and (left == 0 or items[right] >= items[left - 1]))
        if asc and swap:
            print 'yes'
            print 'swap', left + 1, right + 1
        elif desc and swap:
            print 'yes'
            print 'reverse', left + 1, right + 1
        else:
            print 'no'


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    items = map(int, sys.stdin.readline().strip().split(' '))
    almost_sorted(items)