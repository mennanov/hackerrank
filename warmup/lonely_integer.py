"""
There are N integers in an array A. All but one integer occur in pairs. Your task is to find the number that occurs only once.
We can use XOR to solve this problem in linear time: x ^ x = 0, so the only number which will remain is a lonely number.
"""

if __name__ == '__main__':
    _ = input()
    ints = map(int, raw_input().strip().split(" "))
    print reduce(lambda x, y: x ^ y, ints)