arr = []
with open ("day1.txt") as f:
    for line in f:
        arr.append(int(line))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 2020:
                print(arr[i], arr[j], arr[k], arr[i] * arr[j] * arr[k])
                break