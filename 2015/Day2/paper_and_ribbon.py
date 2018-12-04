def convertDimensionsToNumbers(dimensions):
    dim = dimensions.split('x')
    LWH = [int(num) for num in dim]
    return LWH

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
for dimensions in ['2x3x4', '1x1x10']:
    print "Paper: " + str(wrapping_paper_needed(dimensions))
    print "Ribbon: " + str(ribbon_length_needed(dimensions))

totalPaperNeeded = 0
totalRibbonNeeded = 0
with open('Day2Inputs.txt') as f:
    for line in f:
        dimensions = line.rstrip('\n')
        totalPaperNeeded += wrapping_paper_needed(dimensions)
        totalRibbonNeeded += ribbon_length_needed(dimensions)

print "Paper: " + str(totalPaperNeeded)
print "Ribbon: " + str(totalRibbonNeeded)
