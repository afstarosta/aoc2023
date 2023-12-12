from functools import lru_cache

input = open('input.txt', 'r')
lines = input.readlines()

springs = []

for line in lines:
    values = [int(s) for s in line.split(' ')[1].split(',')] * 5
    puzzle = '?'.join([line.split(' ')[0].replace('\n', '')] * 5)
    springs.append({'values': values, 'puzzle': puzzle})

@lru_cache(maxsize=None)
def rec(line, values, next_pos):
    if not values:
        if "#" in line :
            return 0 
        else:
            return 1
    elif not line:
        if sum(values):
            return 0
        else:
            return 1
    elif values[0] == 0:
        if line[0] in ["?", "."]:
            return rec(line[1:], values[1:], False) 
        else:
            return 0
    elif next_pos:
        if line[0] == ".":
            return 0
        else:
            return rec(line[1:], (values[0] - 1,) + values[1:], True)
    elif line[0] == "#":
        return rec(line[1:], (values[0] - 1,) + values[1:], True)
    elif line[0] == ".":
        return rec(line[1:], values, False)
    else:
        return rec(line[1:], values, False) + rec(line[1:], (values[0] - 1,) + values[1:], True)

acc = 0
for spring_line in springs:
    res = rec(spring_line['puzzle'], tuple(spring_line['values']), False)
    print(spring_line['puzzle'])
    print(res)
    acc += res
    

print(acc)

