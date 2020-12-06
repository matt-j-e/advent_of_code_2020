sets = []
with open("day6.txt") as f:
    answers = []
    ppl_in_grp = 0
    lines = f.read().splitlines()
    lines.append("") #add blank line to end to simplify processing
    for line in lines:
        if line == "":
            answers.append(ppl_in_grp)
            sets.append(answers)
            answers = []
            ppl_in_grp = 0
        else:
            for i in range(len(line)):
                answers.append(line[i])
            ppl_in_grp += 1

count = 0
for answer_group in sets:
    unique = set()
    for ans in answer_group:
        if not isinstance(ans, int):
            unique.add(ans)

    for ans in unique:
        if answer_group.count(ans) == answer_group[-1]: count += 1

print(count)
# answer = 3427