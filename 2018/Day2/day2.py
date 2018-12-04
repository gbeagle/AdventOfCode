sym = 'abcdefghijklmnopqrstuvwxyz'

twiceLetters = 0
thriceLetters = 0

data = [n for n in open('day2inputs.txt').readlines()]

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
