def convertDimensionsToNumbers(dimensions):
    dim = dimensions.split('x')
    dim = [int(num) for num in dim]
    return dim

def wrapping_paper_needed(dimensions):
    (length, width, height) = convertDimensionsToNumbers(dimensions)
    lengthWidth = length * width
    widthHeight = width * height
    heightLength = height * length
    slack = min(lengthWidth, widthHeight, heightLength)

    surfaceArea = 2*lengthWidth + 2*widthHeight + 2*heightLength
    total = surfaceArea + slack
    return total

def ribbon_length_needed(dimensions):
    dimensionList = convertDimensionsToNumbers(dimensions)
    dimensionList.sort()
    wrapLength = 2*dimensionList[0] + 2*dimensionList[1]
    bowLength = dimensionList[0] * dimensionList[1] * dimensionList[2]
    totalLength = wrapLength + bowLength
    return totalLength

#test w/ defaults
print wrapping_paper_needed('2x3x4')
print wrapping_paper_needed('1x1x10')

print ribbon_length_needed('2x3x4')
print ribbon_length_needed('1x1x10')

totalPaperNeeded = 0  #part1
totalRibbonNeeded = 0 #part2
with open('Day2Inputs.txt') as f:
    for line in f:
        dimensions = line.rstrip('\n')
        totalPaperNeeded = totalPaperNeeded + wrapping_paper_needed(dimensions)
        totalRibbonNeeded = totalRibbonNeeded + ribbon_length_needed(dimensions)

print "Paper: " + str(totalPaperNeeded)
print "Ribbon: " + str(totalRibbonNeeded)
