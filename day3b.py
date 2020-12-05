trees = 0
position = 0
skip = False
with open("day3.txt") as f:
    for line in f:
        if skip == True:
            skip = False
            continue
        # 31 chars per line + \n on all but the last
        if line[position % 31] == '#':
            trees += 1
        position += 1
        skip = True

print(trees)

# I cheated slightly on this, the second part of today's challenge.
# Rather than write a script to perform all of the steps, I just ran
# the step 1 script 4 times with different increments and made a note 
# of the results. Then used the above code for the "across 1 down 2"
# step.
# The results were 60 286 76 62 & 45 yielding an answer 3638606400.