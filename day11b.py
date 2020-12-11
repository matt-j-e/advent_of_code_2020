seats_str = ''
seats = []
north = []
south = []
east = []
west = []
nwest = []
neast = []
swest = []
seast = []
rows = 0  

with open ("day11test.txt") as f:
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

def n_vect(pos):
    if pos - spr < 0:
        return north
    else:
        north.append(pos - spr)
        return n_vect(pos - spr)

def ne_vect(pos):
    if pos - spr + 1 < 0:
        return neast
    else:
        neast.append(pos - spr + 1)
        return ne_vect(pos - spr + 1)

def e_vect(pos):
    if (pos + 1) % spr == 0:
        return east
    else:
        east.append(pos + 1)
        return e_vect(pos + 1)

def se_vect(pos):
    if (pos + spr + 1) % spr == 0 or (pos + spr + 1) > len(seats)-1:
        return seast
    else:
        seast.append(pos + spr + 1)
        return se_vect(pos + spr + 1)

def s_vect(pos):
    if (pos + spr) > len(seats)-1:
        return south
    else:
        south.append(pos + spr)
        return s_vect(pos + spr)

def sw_vect(pos):
    if (pos + spr - 1) % spr == spr - 1 or (pos + spr - 1) > len(seats)-1:
        return swest
    else:
        swest.append(pos + spr - 1)
        return sw_vect(pos + spr - 1)

def w_vect(pos):
    if (pos - 1) % spr == spr - 1:
        return west
    else:
        west.append(pos - 1)
        return w_vect(pos - 1)

def nw_vect(pos):
    if (pos - spr - 1) % spr == spr - 1 or (pos - spr - 1) < 0:
        return nwest
    else:
        nwest.append(pos - spr - 1)
        return nw_vect(pos - spr - 1)

# def print_matrix(s):
#     # ONLY RELEVANT FOR THE INITIAL TEST DATA
#     for i in range(10):
#         print(s[0+(i*10)], s[1+(i*10)], s[2+(i*10)], s[3+(i*10)], s[4+(i*10)], s[5+(i*10)], s[6+(i*10)], s[7+(i*10)], s[8+(i*10)], s[9+(i*10)])

def movements(s, round=1):
    visible = []
    ns = s[:]
    for i in range(len(ns)):
        # for j in n_vect(i): visible.append(ns[j])
        # for j in ne_vect(i): visible.append(ns[j])
        # for j in e_vect(i): visible.append(ns[j])
        # for j in se_vect(i): visible.append(ns[j])
        # for j in s_vect(i): visible.append(ns[j])
        # for j in sw_vect(i): visible.append(ns[j])
        # for j in w_vect(i): visible.append(ns[j])
        # for j in nw_vect(i): visible.append(ns[j])
        print(n_vect(i))
        
        if ns[i] == '.':
            s[i] = '.'
        elif ns[i] == 'L' and visible.count('#') == 0:
            s[i] = '#'
        elif ns[i] == '#' and visible.count('#') > 4:
            s[i] = 'L'

    if ns == s: return s.count('#')
    if round > 10: return
    round += 1
    return movements(s, round)

print(movements(seats), "occupied seats")