valid = 0
with open("day2.txt") as f:
    for line in f:
        temp = line.strip().split(" ")
        char = temp[1][0]
        char_count = 0
        for i in range(len(temp[2])):
            if char == temp[2][i]:
                char_count += 1
        char_range = temp[0].split("-")
        if char_count < int(char_range[0]) or char_count > int(char_range[1]):
            continue
        else:
            valid += 1

print(valid)
# answer = 460