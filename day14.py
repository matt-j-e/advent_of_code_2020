import re
mem = [0]*99999
mask = ''

def get36bit(dec_num):
    b = bin(dec_num)
    r = '0'*(38-len(b))
    return b.replace('0b', r)


def apply_mask(mask, bin_val):
    if len(mask) != len(bin_val): return "String lengths don't match"
    m_list = list(mask)
    v_list = list(bin_val)
    for i in range(len(m_list)):
        if m_list[i] == 'X':
            continue
        else:
            v_list[i] = m_list[i]
    return "".join(v_list)
        

with open("day14.txt") as f:
    for line in f:
        if line.startswith('mask'):
            mask = line[7:].strip()
        else:
            mem_pos = re.search('\d+', line) # mem_pos[0] = memory position where value to be saved
            value = int(line.split(' = ')[1].strip()) # decimal value
            binary_value = get36bit(value)
            masked_binary = apply_mask(mask, binary_value)
            new_value = int(masked_binary, 2)
            mem[int(mem_pos[0])] = new_value
    print("Part One answer = ", sum(mem)) # 13105044880745


