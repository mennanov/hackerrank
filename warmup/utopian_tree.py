"""
The Utopian Tree goes through 2 cycles of growth every year.
The first growth cycle occurs during the spring, when it doubles in height.
The second growth cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter.
Can you find the height of the tree after N growth cycles?
"""


def utopian_tree(cycles):
    """
    Straight forward implementation
    """
    height = 1
    for i in xrange(cycles):
        if i % 2 == 1:
            height += 1
        else:
            height *= 2
    return height


def utopian_tree_bitwise(cycles):
    """
    From the comment: https://www.hackerrank.com/challenges/utopian-tree/forum/comments/41984
    There is a pattern on the height every year.

    original height: 1

    year 1 (2 cycles) : 1*2+1 = 3
    year 2 (4 cycles) : 3*2+1 = 7
    year 3 (6 cycles) : 7*2+1 = 15
    year 4 (8 cycles) : 15*2+1 = 31
    year 5 (10 cycles) : 31*2+1 = 63

    and you can notice the value in binary is like this

    year 1 (2 cycles) : 1*2+1 = 3     ->      11
    year 2 (4 cycles) : 3*2+1 = 7     ->     111
    year 3 (6 cycles) : 7*2+1 = 15    ->    1111
    year 4 (8 cycles) : 15*2+1 = 31   ->   11111
    year 5 (10 cycles) : 31*2+1 = 63  ->  111111


    you can get the answer by putting 1 as much as (year + 1).
    how to make this? shift 1 by (year + 1) and subtract 1.

    straight forward bit calculation is this:

    (1<<((N>>1)+1))-1
    * N>>1 : devide N by 2 to get year
    1 << (year+1) : if year is 5, it will make 1000000
    -1 will make 1000000 to 111111.

    if cycle is odd, that means the tree will be doubled again.

    ((1<<((N>>1)+1))-1) << n%2
    """

    return ((1 << ((cycles >> 1) + 1)) - 1) << cycles % 2


if __name__ == '__main__':
    import sys

    _ = sys.stdin.readline()
    for n in sys.stdin.readlines():
        print utopian_tree_bitwise(int(n.strip()))
