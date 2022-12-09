
stacks = [
    ['Q','W','P','S','Z','R','H','D'],
    ['V','B','R', 'W','Q','H', 'F'],
    ['C','V','S','H'],
    ['H','F','G'],
    ['P','G','J','B','Z'],
    ['Q','T','J','H','W','F','L'],
    ['Z','T','W','D','L','V','J','N'],
    ['D','T','Z','C','J','G','H','F'],
    ['W','P','V','M','B','H']
]

# Read File
filepath = "C:\\Users\\stran\\Documents\\repos\\advent-of-code-22\\day_05\\input.txt"

# Open file and store into data 
with open(filepath) as file:
    data = (file.read())
    file.close()

# Split out the line breaks
moves = data.splitlines()

for move in moves:
    m = move.split(" ")
    # print(m) # 1 = pieces, 3 = starting stack, 5 = ending stack
    pieces = int(m[1])
    start = int(m[3])
    end = int(m[5])
    temp = []

# Solution for part 2
    for i in range(pieces):
        popped = stacks[start - 1].pop()
        temp.append(popped)
    for i in range(pieces):
        popped = temp.pop()
        stacks[end - 1].append(popped)

print(stacks)

topOfEach = ''
for i in range(len(stacks)):
    topOfEach = topOfEach + (stacks[i][-1])
print(topOfEach)
