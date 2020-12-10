with open("day10.txt") as f:
    series = f.read().splitlines()
    series = sorted(list(map(int, series))) #convert to ints

increm1 = 1
increm3 = 0
for i in range(len(series)-1):
    if series[i] + 1 == series[i+1]: increm1 += 1
    if series[i] + 3 == series[i+1]: increm3 += 1

print(f"Differences of 1: {increm1}")
print(f"Differences of 3: {increm3 + 1}")
print(f"Product = {increm1 * (increm3 + 1)}")
#answer = 2482 (first time success!)