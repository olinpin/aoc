def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("example.in").split("\n")[:-1]
input = parseInput("input.in").split("\n")[:-1]

def part1():
    grid = [[i for i in list(line)] for line in input]
    adjacentCoordinates = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    accessibleRols = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            value = grid[x][y]
            if value != "@":
                continue
            adjacenentRolls = 0
            for a, b in adjacentCoordinates:
                adj = getGrid(grid, (x+a,y+b))
                if adj is not None and adj == "@":
                    adjacenentRolls += 1
            if adjacenentRolls < 4:
                accessibleRols += 1
    print(accessibleRols)


def getGrid(grid, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        return None
    return grid[x][y]

def part2():
    grid = [[i for i in list(line)] for line in input]
    adjacentCoordinates = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    accessibleRols = 0
    x = 0
    while x < len(grid):
        y = 0
        while y < len(grid[x]):
            value = grid[x][y]
            if value != "@":
                y += 1
                continue
            adjacenentRolls = 0
            for a, b in adjacentCoordinates:
                adj = getGrid(grid, (x+a,y+b))
                if adj is not None and adj == "@":
                    adjacenentRolls += 1
            if adjacenentRolls < 4:
                grid[x][y] = "."
                accessibleRols += 1
                x = 0
                y = 0
                break
            y += 1
        else:
            x += 1
            continue
        x = 0
    print(accessibleRols)

def strprint(lines):
    for line in lines:
        print("".join(line))
    print()
part2()
