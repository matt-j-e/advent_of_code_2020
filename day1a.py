arr = []
with open ("day1.txt") as f:
    for line in f:
        arr.append(int(line))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == 2020:
            print(arr[i], arr[j], arr[i] * arr[j])
            break

