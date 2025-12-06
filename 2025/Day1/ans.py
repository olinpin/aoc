# ans

def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("example.in").split("\n")[:-1]
input = parseInput("input.in").split("\n")[:-1]

def part1():
    dial = 50
    pointAtZero = 0
    for line in input:
        # side = line[0]
        turn = int(line[1:])
        if side == "L":
            dial -= turn
        else:
            dial += turn
        dial %= 100
        if dial == 0:
            pointAtZero += 1
    print(pointAtZero)

def part2():
    dial = 50
    pointAtZero = 0
    for line in input:
        side = line[0]
        turn = int(line[1:])
        originalDial = dial
        while turn >= 100:
            turn -= 100
            pointAtZero += 1
        if side == "L":
            dial -= turn
        else:
            dial += turn

        if dial == 0:
            pointAtZero += 1
        if dial >= 100:
            dial -= 100
            pointAtZero += 1
        if dial < 0:
            dial += 100
            if originalDial != 0:
                pointAtZero += 1
    print(pointAtZero)
