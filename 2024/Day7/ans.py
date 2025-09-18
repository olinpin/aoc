import re

def parseInput(file):
    with open(file, "r") as f:
        return f.read()


input = parseInput("input.in").split("\n")[:-1]

def part1():
    res = 0
    # input = {int(key): [int(v) for v in val.split(" ")] for key, val in input.items()}
    inputs = []
    for i in input:
        parts = re.findall(r'\d+', i)
        inputs.append({int(parts[0]): [int(v) for v in parts[1:]]})
    for line in inputs:
        r = list(line.keys())[0]
        vals = list(line.values())[0]
        if getSum(r, 0, vals):
            res += r
    print(res)

def getSum(expected, result, values):
    if expected < result:
        return False
    if len(values) == 0:
        return expected == result
    result1 = getSum(expected, result+values[0], values[1:])
    result2 = getSum(expected, result*values[0], values[1:])
    return result1 or result2
        

part1()
