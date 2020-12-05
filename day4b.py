import re

def validate_string(field, value):
    if field == "byr": return int(value) > 1919 and int(value) < 2003
    elif field == "iyr": return int(value) > 2009 and int(value) < 2021
    elif field == "eyr": return int(value) > 2019 and int(value) < 2031
    elif field == "hgt":
        if len(value) < 4 or len(value) > 5: return False
        unit = value[len(value)-2:]
        if unit != "in" and unit != "cm": return False
        number = int(value[:len(value)-2])
        if unit == "cm": return number > 149 and number < 194
        if unit == "in": return number > 58 and number < 77
    elif field == "hcl": return True #regex has already matched this
    elif field == "ecl": return value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"
    elif field == "pid": return True #regex has already matched this
    elif field == "cid": return True #ignored
    else: return False

pass_str = ''
pass_strings = []
valid_count = 0
with open("day4.txt") as f:
    for line in f:
        if line.strip() != "":
            if pass_str == '':
                pass_str += line.strip()
            else:
                pass_str += " "
                pass_str += line.strip()
        else:
            pass_strings.append(pass_str)
            pass_str = ''

# I now have a List of passport strings with space-separated values
# print(len(pass_strings))
valid_strings = []
patterns = ['byr:[0-9]{4}', 'iyr:[0-9]{4}', 'eyr:[0-9]{4}', 'hgt:[0-9]+[a-z]+', 'hcl:#[0-9a-f]{6}', 'ecl:[a-z]{3}', 'pid:[0-9]{9}']
for string in pass_strings:
    # print(string)
    for pattern in patterns:
        m = re.findall(pattern, string)
        if len(m) != 1:
            valid = False
        else:
            kvp = m[0].split(":")
            field = kvp[0]
            value = kvp[1]
            valid = validate_string(field, value)
        if not valid: break
    
    if valid == True:
        valid_count += 1
        valid_strings.append(string)
        # print(string)

print(valid_count)
print(len(valid_strings))

for s in valid_strings:
    m = re.findall('hcl:#[0-9a-f]{6}', s)
    print(m)  

# tried 157 (many times)
# tried 158
# maybe 156? Correct! So wtf was I doing wrong?????? Why did my script keep spitting out 157???????
