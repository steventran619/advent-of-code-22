# Read File
filepath = "/Users/steventran/Repos/advent-of-code-22/day_06/input.txt"

# Open file and store into data 
with open(filepath) as file:
    data = (file.read())
    file.close()

letters = {}
currentFour = {}
uniques = 4
left = 0

for right in range(len(data)):
    currentLetter = data[right]
    letters[currentLetter] = letters.get(currentLetter, 0) + 1
    if currentLetter in currentFour:
        while currentLetter in currentFour:
            leftLetter = data[left]
            currentFour[leftLetter] = currentFour[leftLetter] - 1
            if currentFour[leftLetter] == 0:
                del currentFour[leftLetter]
            left += 1
    currentFour[currentLetter] = 1
    
    if (len(letters) >= 4 and len(currentFour) == 14):
        print(right + 1)
        break

# need at least 4 letters to unlock
# need 4 unique letters

