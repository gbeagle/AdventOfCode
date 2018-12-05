from itertools import combinations

sym = 'abcdefghijklmnopqrstuvwxyz'

twiceLetters = 0
thriceLetters = 0

data = [n for n in open('2018day2inputs.txt').readlines()]

for id in data:
    twice = False
    thrice = False
    for letter in sym:
        appears = id.count(letter)
        if appears == 2:
            twice = True
        if appears == 3:
            thrice = True
    if twice:
        twiceLetters += 1
    if thrice:
        thriceLetters += 1

print twiceLetters
print thriceLetters
print twiceLetters * thriceLetters

for id1, id2 in combinations(data, 2):
    diff = 0
    diffChars = []
    total = len(id1)
    for n, ch in enumerate(id1):
        if ch != id2[n]:
            diff += 1
            continue
        diffChars.append(id1[n])
    if diff == 1:
        print id1
        print id2
        print ''.join(diffChars)
        break
