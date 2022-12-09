import string
import heapq

# Read File
filepath = "/Users/steventran/Repos/advent-of-code-22/day_03/input.txt"

# Open file and store into data 
with open(filepath) as file:
    data = (file.read())
    file.close()

# Split out the line breaks
compartments = data.splitlines()
print(len(compartments))

def countUniqueLetters(word):
    uniqueLetters = emptyLetters.copy()
    for i in range(len(word)):
        uniqueLetters[word[i]] = uniqueLetters.get(word[i]) + 1
    return uniqueLetters

# Letter Dictionaries
emptyLetters = {}
for letter in string.ascii_letters:
    emptyLetters[letter] = 0;
print(emptyLetters)
secondEmptyLetters = emptyLetters.copy()

for i in range(len(compartments)):
    items = len(compartments[i])
    first = compartments[i][0:items//2]
    # firstSorted = (''.join(sorted(first)))
    second = compartments[i][items//2:]
    # secondSorted = (''.join(sorted(second)))
    for letter in first:
        if letter in second:
            emptyLetters[letter] = emptyLetters.get(letter) + 1
            break

print(emptyLetters)
sum = 0
counter = 1
totalCounts = 0
for letter in string.ascii_letters:
    subtotal = emptyLetters[letter] * counter
    print(f"{letter} : {emptyLetters[letter]} x {counter} = {subtotal}")
    sum += subtotal
    counter += 1
    totalCounts += emptyLetters[letter]

print(sum)
print(totalCounts)


# PART TWO
for i in range(0, len(compartments), 3):
    # first = (''.join(sorted(set(compartments[i]))))
    # second = (''.join(sorted(set(compartments[i + 1]))))
    # third = (''.join(sorted(set(compartments[i + 2]))))
    # print(first, second, third)
    sortedLetters = []
    for j in range(3):
        word = (''.join(sorted(set(compartments[i + j]))))
        heapq.heappush(sortedLetters, [len(word), word])
    
    letters = {}

    firstCount, shortestWord = heapq.heappop(sortedLetters)
    secondCount, secondWord = heapq.heappop(sortedLetters)
    thirdCount, thirdWord = heapq.heappop(sortedLetters)

    print(firstCount, secondCount, thirdCount)
    for letter in shortestWord:
        print(letter)
        if letter in secondWord:
            letters[letter] = letters.get(letter, 0) + 1
    
    for lett in letters:
        print(f"{lett}")
        if lett in thirdWord:
            secondEmptyLetters[lett] = secondEmptyLetters.get(lett, 0) + 1
            break

print(secondEmptyLetters)
sum = 0
counter = 1
totalCounts = 0

for letter in string.ascii_letters:
    subtotal = secondEmptyLetters[letter] * counter
    print(f"{letter} : {secondEmptyLetters[letter]} x {counter} = {subtotal}")
    sum += subtotal
    counter += 1
    totalCounts += emptyLetters[letter]

print(sum)
print(totalCounts)