import re

text = 'turn off 660,55 through 986,197'
pattern = re.compile('(turn on|toggle|turn off)\s(.,.)\sthrough\s(.,.)$')
print re.split(pattern, text)

lightsOn = []
