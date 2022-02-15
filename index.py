# I'm not sure if len(list) count as built-in function there so I made this function

def length(array):
    X = 0
    arrayLength = 0
    while array[X:]:
        arrayLength += 1
        X += 1
    return arrayLength

# Answer 1


def getPairsFromSum(array, sum):

    pairFound = False
    for i in range(0, length(array)):
        for j in range(i, length(array)):
            if array[i] + array[j] == sum:
              # do not get the same number
                if not array[i] == array[j]:
                    pairFound = True
                    print(array[i], array[j])
    if pairFound == False:
        print('No pairs found')

# Answer 2


def getSimilarity(string1, string2):
    i = 0
    # convert to lowercase
    newString1 = ""
    while string1[i:]:
        unicodeCha = ord(string1[i])
        if unicodeCha > 64 and unicodeCha < 91:  # if that character is uppercase, lower it
            newString1 += chr(unicodeCha+32)
        else:
            newString1 += chr(unicodeCha)
        i += 1
    i = 0
    # convert to lowercase
    newString2 = ""
    while string2[i:]:
        unicodeCha = ord(string2[i])
        if unicodeCha > 64 and unicodeCha < 91:  # if that character is uppercase, lower it
            newString2 += chr(unicodeCha+32)
        else:
            newString2 += chr(unicodeCha)
        i += 1

    i = 0
    if length(newString1) == length(newString2):
        foundLetter = False
        while newString1[i:]:
            foundLetter = False
            replacement = ''
            j = 0
            while newString2[j:]:
                if newString1[i] == newString2[j] and foundLetter == False:
                    foundLetter = True
                else:
                    replacement += newString2[j]
                j += 1
            # rebuild newString2 after finishing loop
            newString2 = '%s' % replacement
            if foundLetter == False:
                return False
            i += 1
    else:
        return False
    return True

# Answer 3


def getAirDate(array):

    airDate = []

    prevNumber = 0
    firstDay = array[0]
    range = 0
    i = 0

    for num in array:
        # dont check connected days on the first day\
        i += 1

        # don't check on the first day
        if ((num - prevNumber) > 1 and prevNumber > 0):
            if range == 1:
                airDate.append(str(prevNumber))
            else:
                airDate.append(str(firstDay) + " - " + str(prevNumber))
            firstDay = num
            range = 0

        range += 1

        prevNumber = num

        if i == length(array):
            if range == 1:
                airDate.append(str(prevNumber))
            else:
                airDate.append(str(firstDay) + " - " + str(prevNumber))

    print(airDate)

# Answer 4


def drawTriangle(size):

    if size < 1:
        print('Error: size must be 1 or over')
    else:
        for i in range(0, size):

            for j in range(0, i):
                print(' ', end='')

            for j in range(i, (size*2 - 1) - i):
                print('*', end='')
            print('')

# Answer 5


def drawNumberTriangle(size):
    currentNum = 1

    if size < 1 or size > 4:
        print('Error: size out of range. (1-4)')
    else:

        for i in range(0, size):
            for j in range(i, (size - 1)):
                print(' ', end='')

            for j in range(0, i + 1):
                if currentNum == 10:
                    currentNum = 0
                print(currentNum, end='')
                currentNum += 1
                print(' ', end='')
            print('')

# Answer 6


def sortDesc(array):

    if length(array) != 10:
        print('Error: array size is not equal to 10. You have ' + str(length(array)))
    else:
        # using selection sort algorithm
        for i in range(length(array)):

            highest_i = i
            for j in range(i+1, length(array)):
                if array[highest_i] < array[j]:
                    highest_i = j

            array[i], array[highest_i] = array[highest_i], array[i]

        print(array)

# Answer 7


def displayTime(seconds):
    hours = seconds // 3600  # instead of using floor function

    secondsUnderHour = seconds - (hours * 3600)

    minutes = secondsUnderHour // 60

    secondCount = secondsUnderHour - (minutes * 60)

    print(f'{hours:0>2d}' + ':' + f'{minutes:0>2d}' +
          ':' + f'{secondCount:0>2d}')

# Answer 8


def chargeCounts(input):
    charge = 1000 - input
    chargeCalc = charge

    currencyValue = [500, 100, 50, 10, 5, 1]

    if charge < 0:
        print('Error: cannot afford')
    elif input < 0:
        print('Error: invalid price')
    else:
        print("จำนวนเงินทอน " + str(charge) + " บาท")
        for value in currencyValue:
            currencyCount = chargeCalc // value
            chargeCalc = chargeCalc - (currencyCount * value)

            print(value, end=' ')
            print(currencyCount, end=' ')
            if (value == 500 or value == 100 or value == 50):
                print('ใบ')
            else:
                print('เหรียญ')

# Answer 9


def revertWords(sentence):
    i = 0
    wordIndex = 0

    wordList = []
    wordList.append('')

    while sentence[i:]:
        if sentence[i] == ' ':
            wordIndex += 1
            wordList.append('')
        else:
            wordList[wordIndex] += sentence[i]
        i += 1

    print(wordList)

    revertedWordList = [''] * (length(wordList))

    i = 0
    for word in wordList:
        revertedWordList[i] = word[length(word)::-1]
        i += 1
    print(revertedWordList)

    finalSentence = ''
    wordIndex = 0
    for reword in revertedWordList:
        finalSentence = finalSentence + reword + \
            ('' if wordIndex + 1 == length(revertedWordList) else ' ')
        wordIndex += 1
    print(finalSentence)

# Answer 10


def drawTriangleUp(size):
    if size < 1:
        print('Error: size must be 1 or over')
    else:
        for i in range(0, size):
            for j in range(i, (size - 1)):
                print(' ', end='')

            for j in range(0, (i*2) + 1):
                print('*', end='')
            print('')

# Answer 11


def sortAsc(array):

    if length(array) != 10:
        print('Error: array size is not equal to 10. You have ' + str(length(array)))
    else:
        # using selection sort algorithm
        for i in range(length(array)):

            lowest_i = i
            for j in range(i+1, length(array)):
                if array[lowest_i] > array[j]:
                    lowest_i = j

            array[i], array[lowest_i] = array[lowest_i], array[i]

        print(array)

# ---------- All functions are activated here ---------------

# getPairsFromSum([1, 2, 3, 4, 5], 5)
# getPairsFromSum([4, 5, 6, 7, 8, 9], 12)
# getPairsFromSum([1, 2, 3, 4, 5], 12)

# print(getSimilarity("Mary", "army"))
# print(getSimilarity("Car", "Arcc"))
# print(getSimilarity("mars", "rams"))

# getAirDate([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
# getAirDate([1, 4, 6, 9, 10, 14, 16, 17])

# drawTriangle(5)


# drawNumberTriangle(4)
# drawNumberTriangle(5)

# sortDesc([1, 2, 9, 4, 5, 8, 7, 6, 3,10])

# displayTime(90)
# displayTime(884)
# displayTime(7000)

# chargeCounts(520)

# revertWords('Welcome to clicknext')
# revertWords('This is a fox.')

# drawTriangleUp(5)

sortAsc([1, 2, 9, 4, 5, 8, 7, 6, 3, 10])
