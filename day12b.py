
with open("day12.txt") as f:
    steps = f.read().splitlines()

position = [0, 0] # index[0] = n/s n=+ive; index[1] = e/w east=+ive
heading = [1, 10]
for step in steps:
    instr = step[:1]
    val = int(step[1:])

    if instr == 'N': heading[0] += val
    if instr == 'S': heading[0] -= val
    if instr == 'E': heading[1] += val
    if instr == 'W': heading[1] -= val
    if instr == 'L':
        if val == 90: heading = [heading[1], -heading[0]]
        if val == 180: heading = [-heading[0], -heading[1]]
        if val == 270: heading = [-heading[1], heading[0]]
    if instr == 'R':
        if val == 90: heading = [-heading[1], heading[0]]
        if val == 180: heading = [-heading[0], -heading[1]]
        if val == 270: heading = [heading[1], -heading[0]]
    if instr == 'F':
        position[0] += val * heading[0]
        position[1] += val * heading[1]
    # print(position)

print("Part 2 - Manhattan distance = ", abs(position[0]) + abs(position[1])) # 56135 (correct first try)