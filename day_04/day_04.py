# Read File
filepath = "/Users/steventran/Repos/advent-of-code-22/day_04/input.txt"

# Open file and store into data 
with open(filepath) as file:
    data = (file.read())
    file.close()

# Split out the line breaks
compartments = data.splitlines()
print(compartments)

fullyContains = 0
partialContains = 0
for pairs in compartments:
    pair = pairs.split(',')
    # print(pair)
    nums = []
    for g in pair:
        y = g.split('-')
        nums.append([int(y[0]), int(y[1])])
    print(nums)

    first = nums[0]
    second = nums[1]
    # Part 1
    if (first[0] >= second[0] and first[1] <= second[1]) or (
        (second[0] >= first[0] and second[1] <= first[1])):
        fullyContains += 1
    # Part 2
    if (first[0] >= second[0] and first[0] <= second[1]) or (
        second[0] >= first[0] and second[0] <= first[1]):
        partialContains += 1

print(f"Count of Fully Contained: {fullyContains}")
print(f"Count of Partial Contained: {partialContains}")

    #     56      4-6
    # 12345       1-5

