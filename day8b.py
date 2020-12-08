with open("day8.txt") as f:
    prog = f.read().splitlines()

def run(prog, line=0, accumulator=0, visited_lines=[]):
    visited_lines.append(line)
    line_type = prog[line].split()[0]
    line_value = int(prog[line].split()[1])

    if line_type == 'nop': line += 1
    if line_type == 'acc':
        accumulator += line_value
        line += 1
    if line_type == 'jmp': line += line_value
    # print(f"Type: {line_type}  Value: {line_value}  Line No: {line}  Visited: {visited_lines}")
    if line in visited_lines: return False
    if line >= len(prog): return accumulator
    return run(prog, line, accumulator, visited_lines)

for i in range(len(prog)):
    if prog[i].split()[0] == "nop":
        prog[i] = "jmp " + prog[i].split()[1]
        r = run(prog, 0, 0, [])
        if r: print(f"Part Two - the answer is: {r}")
        prog[i] = "nop " + prog[i].split()[1]
    elif prog[i].split()[0] == "jmp":
        prog[i] = "nop " + prog[i].split()[1]
        r = run(prog, 0, 0, [])
        if r: print(f"Part Two - the answer is: {r}")
        prog[i] = "jmp " + prog[i].split()[1]
    
# answer = 2477
