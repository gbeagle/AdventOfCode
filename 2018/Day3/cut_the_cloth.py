import re

fabric = [[[] for x in range(1001)] for y in range(1001)]
pattern = re.compile("#([\d]+)\s@\s([\d]+),([\d]+):\s([\d]+)x([\d]+)")

data = [pattern.search(line).groups() for line in open('2018day3.txt').readlines()]

unique = {0}
for coord in data:
    (claim, xstart, ystart, xlen, ylen) = coord
    for x in range(int(xstart), (int(xstart)+int(xlen))):
        for y in range(int(ystart), (int(ystart)+int(ylen))):
            if not fabric[x][y]:
                unique.add(claim)
            fabric[x][y].append(claim)

overlap = 0
for x in range(1001):
    for y in range(1001):
        if len(fabric[x][y]) > 1:
            overlap += 1
            for claim in fabric[x][y]:
                if claim in unique:
                    unique.remove(claim)

print overlap
print unique
