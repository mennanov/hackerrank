"""
Given an array with n elements, can you sort this array in ascending order using only one of the following operations?
1. Swap two elements.
2. Reverse one sub-segment.
"""


def can_swap(items, left, right):
    return ((left == 0 or items[right] >= items[left - 1]) and items[right] <= items[left + 1]) \
           and \
           ((right == len(items) - 1 or items[left] <= items[right + 1]) and items[left] >= items[right - 1])


def can_reverse(items, left, right):
    return \
        (left == 0 or items[right] >= items[left - 1]) and \
        (right == len(items) - 1 or items[left] <= items[right + 1])


def almost_sorted(items):
    if len(items) <= 1:
        # array is already sorted
        print 'yes'
        return
    # find swaps
    n = len(items)
    left = 0
    swap = None
    inversions = 0
    for i in xrange(1, n):
        if items[i] < items[i - 1]:
            inversions += 1
            # inversion found
            if swap is not None:
                # we already have 1 swap
                swap = None
                break
            # check if we can swap
            if can_swap(items, left, i):
                # swap found
                swap = (left, i)
            elif inversions == 1 and can_swap(items, i - 1, i):
                # shift left pointer to the previous item
                # swap found
                swap = (i - 1, i)
                break
            else:
                left = i - 1

    if inversions == 0:
        # array is already sorted
        print 'yes'
        return

    if swap:
        # we can make the array sorted with just one swap
        print 'yes'
        print 'swap', swap[0] + 1, swap[1] + 1
        return

    # find reversible sub-array
    left = 0
    rev = None
    shifted_pointer_flag = False
    inversion_found = False
    for i in xrange(1, n):
        if items[i] < items[i - 1]:
            inversion_found = True
            # inversion found
            if rev is not None:
                # we already have 1 reversion
                rev = None
                break
            # check if we can swap
            if can_swap(items, left, i):
                # rev found
                rev = (left, i)
            else:
                if not shifted_pointer_flag:
                    left = i - 1
                    shifted_pointer_flag = True
        elif inversion_found and items[i] != items[i - 1]:
            if can_reverse(items, left, i - 1):
                rev = (left, i - 1)
            else:
                # can not reverse this sub-array
                rev = None
                break

    if rev:
        # we can reverse a sub-array to make the whole array in order
        print 'yes'
        print 'reverse', rev[0] + 1, rev[1] + 1
    else:
        print 'no'


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    items = map(int, sys.stdin.readline().strip().split(' '))
    print items
    almost_sorted(items)
