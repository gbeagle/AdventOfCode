def part1():
    naught_list = ["ab", "cd", "pq", "xy"]
    vowel_list = "aeiou"
    niceList = 0

    with open('day5inputs.txt') as f:
        for input in f:
            vowelCheck = 0
            sequential = False
            if any(substring in input for substring in naught_list):
                continue
            if any(ch == input[index+1] for index, ch in enumerate(input[:-1])):
                sequential = True
            for ch in input:
                if ch in vowel_list:
                    vowelCheck = vowelCheck + 1
            if sequential and (vowelCheck >= 3):
                niceList = niceList + 1
    return niceList

def part2():
    niceList = 0
    with open('day5inputs.txt') as f:
        for input in f:
            twoPairs = False
            sandwich = False
            for index in range(len(input) - 2):
                if input[index:index + 2] in input[index+2:]:
                    twoPairs = True
                if input[index] == input[index+2]:
                    sandwich = True
            if twoPairs and sandwich:
                niceList = niceList + 1
        return niceList

print part1()
print part2()
