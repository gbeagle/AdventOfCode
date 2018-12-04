from itertools import cycle

freq = 0
uniqueFreq = {0}

data = [int(x) for x in open('day1inputs.txt').readlines()]

for increment in cycle(data):
    freq += increment

    if freq in uniqueFreq:
        print freq
        break
    uniqueFreq.add(freq)
