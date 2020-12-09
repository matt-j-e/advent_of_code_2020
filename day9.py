with open ("day9.txt") as f:
    series = f.read().splitlines()
    series = list(map(int, series)) #convert to ints
    
def find_error(series, pre_len): # pre_len = length of preamble
    for i in range(pre_len, len(series)):
        preamble = series[i-pre_len:i]
        if validate(preamble, series[i]): continue
        return series[i]

def validate(p, n): # p=preamble, n=number
    for i in range(len(p)):
        for j in range(len(p)-1):
            if p[i] + p[j] == n: return True
    return False

# invalid = find_error(series, 5)
# print(invalid)
invalid = find_error(series, 25)
print(f"Part One answer = {invalid}")

def weakness(s, n): # s=series, n=invalid number
    for i in range(len(s)):
        block = find_block(s, i, n)
        if block: return block

def find_block(s, i, n):
    j = i + 1
    block = s[i:j+1]
    for j in range(i+1, len(s)):
        block = s[i:j+1]
        if sum(block) == n: return max(block) + min(block)
    return False

print(f"Part Two answer is: {weakness(series, invalid)}")

# part 1 answer = 1038347917 (got it first time (when I put the right preamble length in!))
# part 2 answer = 137394018 (first time again!)