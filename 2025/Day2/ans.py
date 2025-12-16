# ans

def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("example.in").split("\n")[0].split(",")
input = parseInput("input.in").split("\n")[0].split(",")

def part1():
    res = 0
    invalidIds = []
    for sequence in input:
        firstId = sequence.split("-")[0]
        originalFirstId = firstId
        lastId = sequence.split("-")[1]
        firstLen = len(firstId)
        if firstLen % 2 == 1:
            firstId = "1" + "0" * firstLen
        while int(firstId) <= int(lastId):
            half = firstId[:len(firstId) // 2]
            num = half * 2
            if int(num) <= int(lastId) and int(num) >= int(originalFirstId):
                invalidIds.append(num)
                res += int(num)
            firstId = str(int(half) + 1) * 2
    print(res)

def part2():
    res = 0
    for sequence in input:
        firstId = sequence.split("-")[0]
        lastId = sequence.split("-")[1]
        while int(firstId) <= int(lastId):
            newFirstId = str(int(firstId) + 1)
            if len(set(firstId)) == 1 and len(firstId) > 1:
                res += int(firstId)
                firstId = newFirstId
                continue
            firstLen = len(firstId)
            for i in range(1, (firstLen // 2 + 1)):
                subId = firstId[:i]
                possibleId = subId * (firstLen // i)
                if possibleId == firstId:
                    res += int(possibleId)
                    break
            firstId = newFirstId
    print(res)

part2()
