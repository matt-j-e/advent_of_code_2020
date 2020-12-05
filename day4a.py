import re
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

# patterns = ['byr:[0-9]{4,}', 'iyr:[0-9]{4,}', 'eyr:[0-9]{4,}', 'hgt:[0-9]+[a-z]+', 'hcl:#[0-9a-zA-Z]{6,}', 'ecl:[a-zA-Z]+', 'pid:[0-9]+']
patterns = ['byr:[0-9a-zA-Z#]+', 'iyr:[0-9a-zA-Z#]+', 'eyr:[0-9a-zA-Z#]+', 'hgt:[0-9a-zA-Z#]+', 'hcl:[0-9a-zA-Z#]+', 'ecl:[0-9a-zA-Z#]+', 'pid:[[0-9a-zA-Z#]+']
valid = True
for string in pass_strings:
    for pattern in patterns:
        if not re.search(pattern, string):
            valid = False    
    if valid == True:
        valid_count += 1
    else:
        valid = True

print(valid_count)
