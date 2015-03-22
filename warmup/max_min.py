# -*- coding: utf-8 -*-
"""
Given a list of N integers, your task is to select K integers from the list such that its unfairness is minimized.

if (x1,x2,x3,…,xk) are K numbers selected from the list N, the unfairness is defined as max(x1,x2,…,xk)−min(x1,x2,…,xk)
where max denotes the largest integer among the elements of K, and min denotes the smallest integer among the elements of K.
"""

if __name__ == '__main__':
    import sys
    
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    numbers = []
    for line in sys.stdin.readlines():
        numbers.append(int(line))
        
    numbers.sort()
    min_diff = float('Inf')
    l = k - 1
    for i in xrange(l, len(numbers)):
        diff = numbers[i] - numbers[i - l]
        if diff < min_diff:
            min_diff = diff
    print min_diff