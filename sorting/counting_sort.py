"""
The problem is stated here: https://www.hackerrank.com/challenges/countingsort4
"""


def counting_sort(items):
    # find the max value
    max_val = max(k for k, _ in items)
    counter = []
    # build a look-up list from 0 to max_value
    for _ in xrange(max_val + 1):
        counter.append([])
    # count values
    for i, (num, word) in enumerate(items):
        counter[num].append((word, i))
    half = len(items) / 2
    output = []
    for num, values in enumerate(counter):
        for word, pos in values:
            if pos >= half:
                output.append(word)
            else:
                output.append('-')
    print ' '.join(output)


if __name__ == '__main__':
    import sys

    sys.stdin.readline()
    items = []
    for line in sys.stdin.readlines():
        l = line.split(' ')
        items.append((int(l[0]), l[1].strip()))

    counting_sort(items)