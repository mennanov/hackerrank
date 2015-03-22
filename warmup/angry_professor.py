"""
The professor is conducting a course on Discrete Mathematics to a class of N students.
He is angry at the lack of their discipline, and he decides to cancel the class if there are less than K students
present after the class starts.

Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

Input Format

The first line of the input contains T, the number of test cases. Each test case contains two lines.
The first line of each test case contains two space-separated integers, N and K.
The next line contains N space-separated integers indicating the arrival time of each student.

If the arrival time of a given student is a non-positive integer (N <= 0),
then the student enters before the class starts.
If the arrival time of a given student is a positive integer (N>0),
the student enters after the class has started.
If a student enters the class exactly when it starts (N=0),
the student is considered to have entered before the class has started.

Output Format

For each testcase, print YES if the class gets cancelled and NO otherwise.
"""


def angry_professor(ints, k):
    c = 0
    for i in ints:
        if i <= 0:
            c += 1
    return c >= k


if __name__ == '__main__':
    import sys

    t = int(sys.stdin.readline())
    for _ in xrange(t):
        n, k = map(int, sys.stdin.readline().split(' '))
        ints = map(int, sys.stdin.readline().split(' '))
        print 'NO' if angry_professor(ints, k) else 'YES'