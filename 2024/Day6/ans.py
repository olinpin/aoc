from enum import Enum
from typing import List, Tuple

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")[:-1]

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __str__(self) -> str:
        match self:
            case self.UP:
                return "U"
            case self.DOWN:
                return "D"
            case self.LEFT:
                return "L"
            case self.RIGHT:
                return "R"


def part1():
    matrix = []
    startX = 0
    startY = 0
    for i, line in enumerate(input):
        matrix.append(list(line))
        if '^' in line:
            startX = line.index('^')
            startY = i
            matrix[startY][startX] = "X"
    x = startX
    y = startY
    direction = Directions.UP
    while validCoordinates(x, y, matrix):
        newX, newY = move(x, y, direction)
        if not validCoordinates(newX, newY, matrix):
            break
        if matrix[newY][newX] in (".", "X"):
            matrix[newY][newX] = "X"
            x, y = newX, newY
        elif matrix[newY][newX] == "#":
            direction = switchDirection(direction)
    countX = 0
    for line in matrix:
        countX += line.count("X")
    print(countX)


def getMatrixFromInput(input):
    startX = 0
    startY = 0
    matrix = []
    for i, line in enumerate(input):
        matrix.append(list(line))
        if '^' in line:
            startX = line.index('^')
            startY = i
            matrix[startY][startX] = "X"
    return matrix, startX, startY


def part2():
    matrix, startX, startY = getMatrixFromInput(input)
    x, y = startX, startY
    direction = Directions.UP
    originalPath = []
    while validCoordinates(x, y, matrix):
        newX, newY = move(x, y, direction)
        if not validCoordinates(newX, newY, matrix):
            break
        if matrix[newY][newX] in (".", "X"):
            matrix[newY][newX] = "X"
            x, y = newX, newY
            originalPath.append((x, y))
        elif matrix[newY][newX] == "#":
            direction = switchDirection(direction)
    loop = 0
    # for i, (givenX, givenY) in enumerate(originalPath):
            # print(i)
    for givenY in range(len(matrix)):
        for givenX in range(len(matrix[givenY])):
            # print(givenY, givenX)
            x, y = startX, startY
            if (x,y) == (givenX, givenY):
                continue
            elif (givenY,givenX) not in originalPath:
                continue
            direction = Directions.UP
            newMatrix, _, _ = getMatrixFromInput(input)
            newMatrix[givenX][givenY] = "#"
            visited = []
            while True:
                newX, newY = move(x, y, direction)
                if not validCoordinates(newX, newY, newMatrix):
                    break
                if (newY, newX, direction) in visited:
                    loop += 1
                    # print("LOOP: ", x, y, direction)
                    # strprint(newMatrix)
                    break
                if newMatrix[newY][newX] in (".", "X"):
                    newMatrix[newY][newX] = "X"
                    visited.append((newY, newX, direction))
                    x, y = newX, newY
                elif newMatrix[newY][newX] == "#":
                    direction = switchDirection(direction)
    print(loop)
            

def validCoordinates(x: int, y: int, matrix: List[List[str]]) -> bool:
    return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[x])

def move(x: int, y: int, currentDirection: Directions) -> Tuple[int, int]:
    match currentDirection:
        case Directions.UP:
            return (x, y-1)
        case Directions.DOWN:
            return (x, y+1)
        case Directions.LEFT:
            return (x-1, y)
        case Directions.RIGHT:
            return (x+1, y)
    

def switchDirection(currentDirection: Directions) -> Directions:
    match currentDirection:
        case Directions.UP:
            return Directions.RIGHT
        case Directions.DOWN:
            return Directions.LEFT
        case Directions.LEFT:
            return Directions.UP
        case Directions.RIGHT:
            return Directions.DOWN

def strprint(lines):
    for line in lines:
        print("".join(line))
    print()

part2()
