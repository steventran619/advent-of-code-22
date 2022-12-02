import heapq

filepath = "/Users/steventran/Repos/advent-of-code-22/day_01/01_input.txt"

with open(filepath) as file:
    data = (file.read())
    file.close()

elves = data.split("\n\n")
print(elves)

minHeap = []

for i in range(len(elves)):
    row = (elves[i].split("\n"))
    total = 0
    for food in row:
        total += int(food)
    heapq.heappush(minHeap, [-total, i])

# Part One
topElf = minHeap[0]
print(minHeap[0])

# Part Two
topThree = 0
for i in range(3):
    calories, elf = heapq.heappop(minHeap)
    topThree += calories
print(topThree)

