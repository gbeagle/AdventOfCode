import re
from numpy import count_nonzero

def follow_directions(instruction, lights):
    (lightFlip, x1, y1, x2, y2) = instruction
    for x in range(int(x1), (int(x2)+1)):
        for y in range(int(y1), (int(y2)+1)):
            if lightFlip == 'turn on':
                lights[x][y] = 1
            elif lightFlip == 'turn off':
                lights[x][y] = 0
            elif lightFlip == 'toggle':
                if lights[x][y] == 1: lights[x][y] = 0
                elif lights[x][y] == 0: lights[x][y] = 1
    return lights


pattern = re.compile("(turn on|toggle|turn off)\s([\w]+),([\w]+)\sthrough\s([\w]+),([\w]+)")
testInfo = ['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500']
lights = [[0 for x in range(1000)] for y in range(1000)]

for line in testInfo:
    direction = pattern.search(line).groups()
    lights = follow_directions(direction, lights)

print count_nonzero(lights)
