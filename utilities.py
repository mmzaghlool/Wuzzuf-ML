import re


# Get all available values
def getEnum(column):
    result = {}
    for i in column:
        item = result.get(i, 0)
        result[i] = item + 1

    return list(result.keys())


def removeSpaces(column):
    result = []
    for i in range(len(column)):
        result.append(column[i].replace(" ", ""))

    return result


# represent list in binary
def addBinaryAsFeaturesFromList(enum, column):
    result = {}

    for i in enum:
        subResult = []

        for listCell in column:
            found = False

            for item in listCell:
                if i == item:
                    found = True

            if found:
                subResult.append(1)
            else:
                subResult.append(0)

        result[i] = subResult
    return result


def filterExperienceYears(column):
    result = []

    for cell in column:
        rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", cell)

        result.append(rr[0])
    return result
