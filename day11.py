seats_str = ''
seats = []
rows = 0  

with open ("day11.txt") as f:
    for line in f:
        rows += 1
        seats_str += line.strip()

seats_str = seats_str.replace('L', '#')
for s in seats_str: seats.append(s)

tot_seats = len(seats)
spr = int(tot_seats/rows)
print(tot_seats, "total seats")
print(spr, "seats per row")
print(rows, "rows")

# def print_matrix(s):
#     # ONLY RELEVANT FOR THE INITIAL TEST DATA
#     for i in range(10):
#         print(s[0+(i*10)], s[1+(i*10)], s[2+(i*10)], s[3+(i*10)], s[4+(i*10)], s[5+(i*10)], s[6+(i*10)], s[7+(i*10)], s[8+(i*10)], s[9+(i*10)])

def movements(s, round=1):
    surrounding = []
    ns = s[:]
    for i in range(len(ns)):
        if i == 0 or i == spr - 1 or i == tot_seats - spr or i == tot_seats - 1:
            continue
        if i < spr:
            surrounding = [ns[i-1], ns[i+1], ns[i+spr-1], ns[i+spr], ns[i+spr+1]]
        elif i > tot_seats - spr - 1:
            surrounding = [ns[i-1], ns[i+1], ns[i-spr-1], ns[i-spr], ns[i-spr+1]]
        elif i % spr == 0:
            surrounding = [ns[i-spr], ns[i-spr+1], ns[i+1], ns[i+spr], ns[i+spr+1]]
        elif i % spr == spr-1:
            surrounding = [ns[i-spr-1], ns[i-spr], ns[i-1], ns[i+spr-1], ns[i+spr]]
        else:
            surrounding = [ns[i-1], ns[i+1], ns[i-spr-1], ns[i-spr], ns[i-spr+1], ns[i+spr-1], ns[i+spr], ns[i+spr+1]]
        
        
        if ns[i] == '.':
            s[i] = '.'
        elif ns[i] == 'L' and surrounding.count('#') == 0:
            s[i] = '#'
        elif ns[i] == '#' and surrounding.count('#') > 3:
            s[i] = 'L'

    if ns == s: return s.count('#')
    round += 1
    return movements(s, round)

print(movements(seats), "occupied seats") #2249