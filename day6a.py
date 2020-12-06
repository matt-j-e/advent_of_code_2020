sets = []
with open("day6.txt") as f:
    answers = set()
    lines = f.read().splitlines()
    lines.append("") #add blank line to end to simplify processing
    for line in lines:
        if line == "":
            sets.append(answers)
            answers = set()
        else:
            for i in range(len(line)):
                answers.add(line[i])

sum_of_counts = 0
for set in sets:
    sum_of_counts += len(set)

print(sum_of_counts)
# answer = 6532