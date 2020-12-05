trees = 0
position = 0
with open("day3.txt") as f:
    for line in f:
        # 31 chars per line + \n on all but the last
        if line[position % 31] == '#':
            trees += 1
        position += 3

print(trees)