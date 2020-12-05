# Both parts solved in one script today.

def binary_search(range, code, i=0):
    if range[0] == range[1]:
        return range[0]
    target = code[i]
    size = range[1] - range[0] + 1
    if target == "F" or target == "L":
        range[1] = range[0] + int(size / 2) - 1
    if target == "B" or target == "R":
        range[0] = range[0] + int(size / 2)
    i += 1
    return binary_search(range, code, i) # Need to RETURN the recursive function here otherwise the base case returns None

seat_ids = []
with open("day5.txt") as f:
    for line in f:
        row = binary_search([0, 127], line[:7])
        col = binary_search([0, 7], line[7:])
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)

print(f"Part 1: Highest seat number = {max(seat_ids)}")
#922 was the answer to part 1

seat_ids.sort()
for i in range(len(seat_ids)-1):
    if seat_ids[i] + 1 != seat_ids[i+1]: print(f"Part 2: Your seat is number {seat_ids[i] + 1}")
#747 was the answer to part 2
