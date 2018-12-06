import re

data = sorted(open('2018day4inputs.txt').readlines())

pattern = re.compile("\[1518-(\d\d-\d\d)\s(\d\d):(\d\d)\]\s(wakes up|falls asleep|Guard #[\d]+ begins shift)")
guardParse = re.compile("Guard #([\d]+) begins shift")

guards = {} #guard number:[60-element list, use the index as the minute]

id = 0
start = 0
for scribble in data:
    (date, hour, minute, action) = pattern.search(scribble).groups()
    if 'Guard' in action:
         id = guardParse.search(action).groups()[0]
         if id not in guards.keys():
             guards[id] = [0 for n in range(60)]
    if 'falls asleep' in action:
        start = int(minute)
    if 'wakes up' in action:
        for n in range(start, int(minute)):
            guards[id][n] += 1


#part 1
narcoleptic = 0
totalTimeAsleep = 0
for id, minutes in guards.items():
    if sum(minutes) > totalTimeAsleep:
        narcoleptic = str(id)
        totalTimeAsleep = sum(minutes)

print(int(narcoleptic) * guards[narcoleptic].index(max(guards[narcoleptic])))

#part 2
dozer = (0, 0)
minuteMostAsleep = 0
for id, minutes in guards.items():
    if max(minutes) > minuteMostAsleep:
        minuteMostAsleep = max(minutes)
        dozer = (id, guards[id].index(max(guards[id])))

print(int(dozer[0]) * dozer[1])
