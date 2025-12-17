def parseInput(file):
    with open(file, "r") as f:
        return f.read()

input = parseInput("example.in").split("\n")[:-1]
input = parseInput("input.in").split("\n")[:-1]

def part1():
    ranges = []
    ids = []
    empty = False
    for line in input:
        if line == "":
            empty = True
            continue
        if not empty:
            r = line.split("-")
            ranges.append((int(r[0]), int(r[1])))
        else:
            ids.append(int(line))
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id and id <= end:
                count += 1
                break

    print(count)

part1()
