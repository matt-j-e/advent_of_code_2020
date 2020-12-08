bags = []
with open ("day7test.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        bag = line.replace(' contain', ',', ).split(',')
        bag[0] = bag[0][:-1]
        bags.append(bag)

ancestors = set()

def get_parents(targets):
    # print(targets)
    parents = set()
    for target in targets:
        for bag in bags:
            for item in bag[1:]:
                # print(f"{item} : {target}")
                if target in item:
                    # print(f"Target = {target} : Parent = {bag[0]}")
                    parents.add(bag[0])
    return parents

def all_parents(target):
    global ancestors
    parents = get_parents(target)
    if parents == set():
        return len(ancestors)
    else:
        ancestors.update(parents)
        return all_parents(parents)

t = {"shiny gold bag"}
print(f"Part One - the answer is: {all_parents(t)}")

# PART ONE
# First attemp - 605 - was too high
# answer = 289
