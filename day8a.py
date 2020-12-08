with open("day8.txt") as f:
    prog = f.read().splitlines()

visited_lines = []

def run(line=0, accumulator=0):
    visited_lines.append(line)
    line_type = prog[line].split()[0]
    line_value = int(prog[line].split()[1])

    if line_type == 'nop': line += 1
    if line_type == 'acc':
        accumulator += line_value
        line += 1
    if line_type == 'jmp': line += line_value
    print(f"Type: {line_type}  Value: {line_value}  Line No: {line}  Visited: {visited_lines}")
    if line in visited_lines: return accumulator 
    return run(line, accumulator)

print(run())
# answer = 2080 (right first time!)