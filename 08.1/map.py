input = open('input.txt', 'r')
lines = input.readlines()

instructions = lines.pop(0)
instructions_indexes = []
for i in instructions:
    if i == 'L':
        instructions_indexes.append(0)
    if i == 'R':
        instructions_indexes.append(1)

lines.pop(0)
map_dict = {}
print(instructions)

for line in lines:
    node_name = line.split("=")[0].strip()
    children = line.split("=")[1].replace('(', '').replace(')', '').replace(' ', '').replace('\n', '').split(',')
    map_dict[node_name] = children

found_zzz = False
steps = 0
current_step = 'AAA'
while not found_zzz:
    options = map_dict[current_step]
    direction = instructions_indexes[steps % len(instructions_indexes)]
    print(direction)
    current_step = options[direction]
    if current_step == 'ZZZ':
        found_zzz = True
    else:
        steps += 1
        
print(steps + 1)