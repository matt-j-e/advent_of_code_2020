with open("day13.txt") as f:
    lines = f.read().splitlines()
    earliest = int(lines[0])
    ids = lines[1].split(",") # strings

def partOne():
    depart_time = earliest
    calc = True
    while calc:
        for id in ids:
            if id == 'x': continue
            if depart_time % int(id) == 0:
                return (depart_time - earliest) * int(id)
                calc = False
        depart_time += 1

def schDict(buses):
    delays = []
    for i in range(len(buses)):
        if buses[i] == 'x': continue
        d = {
            "delay": i,
            "id": int(buses[i])
        }
        delays.append(d)
    return delays

def partTwo(ids):
    depart_time = 100000000000000
    ids = schDict(ids)
    # calc = True
    while True:
        if depart_time % 1000000 == 0: print(depart_time / 1000000)
        match = True
        for i in range(len(ids)):
            check = (depart_time + ids[i]["delay"]) % ids[i]["id"]
            if check != 0:
                match = False
                continue
        if match == True: return depart_time
        depart_time += 1
 
print("Part Two answer is:", partTwo(ids))
print("Part One answer is:", partOne())