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
