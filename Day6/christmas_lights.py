import re
from numpy import count_nonzero

def follow_directions(instruction, lights1, lights2):
    (lightFlip, x1, y1, x2, y2) = instruction
    for x in range(int(x1), (int(x2)+1)):
        for y in range(int(y1), (int(y2)+1)):
            if lightFlip == 'turn on':
                lights1[x][y] = 1
                lights2[x][y] += 1
            elif lightFlip == 'turn off':
                lights1[x][y] = 0
                if lights2[x][y] > 0: lights2[x][y] -= 1
            elif lightFlip == 'toggle':
                if lights1[x][y] == 1: lights1[x][y] = 0
                elif lights1[x][y] == 0: lights1[x][y] = 1
                lights2[x][y] += 2
    return lights1, lights2


pattern = re.compile("(turn on|toggle|turn off)\s([\w]+),([\w]+)\sthrough\s([\w]+),([\w]+)")
testInfo = ['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500']
lights1 = [[0 for x in range(1000)] for y in range(1000)]
lights2 = [[0 for x in range(1000)] for y in range(1000)]

with open('day6inputs.txt') as f:
    for line in f:
        direction = pattern.search(line).groups()
        (lights1, lights2) = follow_directions(direction, lights1, lights2)

print count_nonzero(lights1)
print sum(sum(x) for x in lights2)
