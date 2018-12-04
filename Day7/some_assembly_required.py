#https://adventofcode.com/2015/day/7

import re

MAX_SIGNAL = 65535

def follow_instructions(instruction, gates):
    if instruction.isdigit():
        return int(instruction)
    if not bool(gates):
        return

    process_instruction(instruction)
    # if 'NOT' in st:
    #     if (~ gates[st[1]]) <= 0:
    #         return MAX_SIGNAL + (~ gates[st[1]]) + 1
    #     return ~ gates[st[1]]
    # if 'AND' in st:
    #     return gates[st[0]] & gates[st[2]]
    # if 'OR' in st:
    #     return gates[st[0]] | gates[st[2]]
    # if 'LSHIFT' in st:
    #     return gates[st[0]] << int(st[2])
    # if 'RSHIFT' in st:
    #     return gates[st[0]] >> int(st[2])

def process_instruction(instruction):
    infoPattern = re.compile("(.*)(NOT|\sAND|\sOR|\sLSHIFT|\sRSHIFT)\s(.*)")
    (wire1, op, wire2) = infoPattern.search(instruction).groups()
    if wire1.isdigit():
        wire1 = int(wire1)
    if wire2.isdigit():
        wire2 = int(wire2)
    print (wire1, op, wire2)

pattern = re.compile("(.*)\s->\s(.*)")
gates = {}
testInfo = ['123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i']

#with open('day7inputs.txt') as f:
for instruction in testInfo:
    instruction.strip('\n')
    (instruction, wire) = pattern.search(instruction).groups()
    #print(instruction, wire)
    val = follow_instructions(instruction, gates)
    if (val):
        gates[wire] = val
