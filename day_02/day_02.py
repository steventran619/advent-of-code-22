import heapq

# Read File
filepath = "/Users/steventran/Repos/advent-of-code-22/day_02/input.txt"

# Open file and store into data 
with open(filepath) as file:
    data = (file.read())
    file.close()

# Split out the line breaks
rounds = data.splitlines()
print(len(rounds))

rules = {
    "A": 1,     # R1 > S3
    "B": 2,     # P2 > R1
    "C": 3,     # S3 > P2
    "X": 1,     # Lose
    "Y": 2,     # Tie
    "Z": 3      # Win
}
score = 0
for round in rounds:
    opponent = rules[round[0]]
    me = rules[round[2]]
    # print(opponent, me)
    result = ''
    if me - opponent == 1 or (me - opponent == -2):
        score += 6
        result = 'won'
    elif (me - opponent > 1) or (me - opponent == -1) :
        score += 0
        result = 'lost'
    elif me - opponent == 0:
        score += 3
        result = 'draw'
    print(f"My {me} VS Their {opponent}: {result}")
    score += me

print(f"score is {score}")

# PART TWO
scoreTwo = 0
for round in rounds:
    opponent = rules[round[0]]
    me = rules[round[2]]
    # WIN CONDITION
    if me == 3:
        condition = 'WIN'
        myMove = (opponent + 1) % 3
        if myMove == 0:
            myMove = 3
        scoreTwo += 6
    elif me == 2:
        condition = 'DRAW'
        myMove = opponent
        scoreTwo += 3
    elif me == 1:
        condition = 'LOSE'
        myMove = (opponent - 1) % 3
        if myMove == 0:
            myMove = 3
    print(f"{condition} {myMove} VS {opponent}")
    scoreTwo += myMove
print(scoreTwo)
        




    
