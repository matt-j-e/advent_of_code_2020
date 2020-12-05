valid = 0
with open("day2.txt") as f:
    for line in f:
        temp = line.strip().split(" ")
        char = temp[1][0]
        char_posn = temp[0].split("-")
        matches = 0
        for i in range(len(temp[2])):
            if i != int(char_posn[0]) - 1 and i != int(char_posn[1]) - 1:
                continue
            if char == temp[2][i]:
                matches += 1
        if matches == 1:
            valid += 1

print(valid)