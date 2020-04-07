from difflib import SequenceMatcher
import sys


egGov = ['alexandria', 'cairo', 'almansora', 'ismeilia', 'aswan', 'asyut', 'luxor', 'behira', 'benisuif', 'portsaid',
         'garbia', 'sharkia', 'dakahlia', 'qalyubia', 'giza', 'damietta', 'monufia', 'faiyum', 'minya', 'sinai', 'suez',
        'redsea', 'matrouh', 'newvally', 'kafrelsheikh', 'qena', 'sohag', '6october', 'tanta', '10ramadan', 'damanhour']


# Get all available values
def getEnum(columnName):
    result = {}
    for i in data[columnName]:
        # i = str(i).lower()
        item = result.get(i, 0)
        result[i] = item + 1

    return list(result.keys())


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def removeUnWantedWords(wordList=[]):
    newList = []
    for i in wordList:
        i = str(i)

        if len(i) < 3:
            continue

        if i == "city":
            continue

        if (i.__contains__("any")) | (i.__contains__("all"))| (i.__contains__("egypt")):
            newList.append("anyLocation")
        else:
            newList.append(i)

    return newList


def checkSimilarity(wordList):
    newWordList = []

    for word in wordList:
        similarTo = ""
        similarPerc = 0.0

        if word == "anyLocation":
            newWordList = ["anyLocation"]
            break

        for gov in egGov:
            sim = similar(word, gov)
            if sim > similarPerc:
                similarTo = gov
                similarPerc = sim

        if similarPerc <= 0.6:
            newWordList.append("anyLocation")
        else:
            newWordList.append(similarTo)

    return newWordList


def removeDuplicated(wordList):
    newWordList = []

    for word in wordList:
        found = False

        for newWord in newWordList:
            if word == newWord:
                found = True
                break

        if not found:
            newWordList.append(word)

    return newWordList


def split(word: str):
    word = word.lower()

    newWord = word.replace(" and ", ",")
    newWord = newWord.replace(" ", "")
    newWord = newWord.replace("city", "")
    newWord = newWord.replace("th", "")
    newWord = newWord.replace("of", "")
    newWord = newWord.replace("-", ",")
    newWord = newWord.replace("/", ",")
    newWord = newWord.replace("&", ",")

    wordList = newWord.split(",")
    wordList = removeUnWantedWords(wordList)
    wordList = checkSimilarity(wordList)
    wordList = removeDuplicated(wordList)

    return wordList


def filterCities(cities):
    newCities = []

    for i in cities:
        newCities.append(split(i))

    return newCities


# sys.modules[__name__] = filterCities, egGov
