
with open("day12.txt") as f:
    steps = f.read().splitlines()

position = [0, 0] # index[0] = n/s n=+ive; index[1] = e/w east=+ive
heading = 90
for step in steps:
    instr = step[:1]
    val = int(step[1:])

    if instr == 'N': position[0] += val
    if instr == 'S': position[0] -= val
    if instr == 'E': position[1] += val
    if instr == 'W': position[1] -= val
    if instr == 'L': heading -= val
    if instr == 'R': heading += val
    if instr == 'F':
        if abs(heading % 360) == 0: position[0] += val
        if abs(heading % 360) == 90: position[1] += val
        if abs(heading % 360) == 180: position[0] -= val
        if abs(heading % 360) == 270: position[1] -= val
    # print(position)

print("Part 1 - Manhattan distance = ", abs(position[0]) + abs(position[1])) # 962 (first time)