"""
Flip all bits of 32-bit integer number.
This can be easily done with XOR operation: XOR with 1111..1 always flips all the bits in a number.
"""

LENGTH = 32

# generate a long 32 bit integer with all ones
mask = sum((2 ** i for i in xrange(LENGTH)))
        
if __name__ == '__main__':
    import sys
    
    sys.stdin.readline()
    for line in sys.stdin.readlines():
        n = int(line)
        print n ^ mask