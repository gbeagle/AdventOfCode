def evaluate_paren(paren, floor):
    """"Evaluates parentheses"""
    if paren == "(":
        return floor + 1
    elif paren == ")":
        return floor - 1


def follow_directions(directions):
    """"Follows directions"""
    floor = 0
    for parentheses in directions:
        floor = evaluate_paren(parentheses, floor)
    return floor


def find_basement(directions):
    """"Finds basement"""
    currentLevel = 0
    for position, paren in enumerate(directions):
        if currentLevel == -1:
            return position
        else:
            currentLevel = evaluate_paren(paren, currentLevel)


with open('inputDay1.txt') as f:
    for directions in f:
        print "Part 1: " + str(follow_directions(directions.strip('\n')))
        print "Part 2: " + str(find_basement(directions.strip('\n')))
