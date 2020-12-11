seats = list(range(100))

spr = 10
north = []
south = []
east = []
west = []
nwest = []
neast = []
swest = []
seast = []
def n(pos):
    if pos - spr < 0:
        print(north)
        return
    else:
        north.append(pos - spr)
        return n(pos - spr)

def ne(pos):
    if pos - spr + 1 < 0:
        print(neast)
        return
    else:
        neast.append(pos - spr + 1)
        return ne(pos - spr + 1)

def e(pos):
    if (pos + 1) % spr == 0:
        print(east)
        return
    else:
        east.append(pos + 1)
        return e(pos + 1)

def se(pos):
    if (pos + spr + 1) % spr == 0 or (pos + spr + 1) > len(seats)-1:
        print(seast)
        return
    else:
        seast.append(pos + spr + 1)
        return se(pos + spr + 1)

def s(pos):
    if (pos + spr) > len(seats)-1:
        print(south)
        return
    else:
        south.append(pos + spr)
        return s(pos + spr)

def sw(pos):
    if (pos + spr - 1) % spr == spr - 1 or (pos + spr - 1) > len(seats)-1:
        print(swest)
        return
    else:
        swest.append(pos + spr - 1)
        return sw(pos + spr - 1)

def w(pos):
    if (pos - 1) % spr == spr - 1:
        print(west)
        return
    else:
        west.append(pos - 1)
        return w(pos - 1)

def nw(pos):
    if (pos - spr - 1) % spr == spr - 1 or (pos - spr - 1) < 0:
        print(nwest)
        return
    else:
        nwest.append(pos - spr - 1)
        return nw(pos - spr - 1)

n(0)
