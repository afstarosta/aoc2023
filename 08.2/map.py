input = open('input.txt', 'r')
lines = input.readlines()

positions = []
instructions = lines.pop(0)
instructions_indexes = []
for i in instructions:
    if i == 'L':
        instructions_indexes.append(0)
    if i == 'R':
        instructions_indexes.append(1)

lines.pop(0)
map_dict = {}

for line in lines:
    node_name = line.split("=")[0].strip()
    if node_name[2] == 'A':
        positions.append([node_name, []])
    children = line.split("=")[1].replace('(', '').replace(')', '').replace(' ', '').replace('\n', '').split(',')
    map_dict[node_name] = children


for i, position in enumerate(positions):
    z_found = False
    steps = 0
    last_step_count = 0     
    while not z_found:
        options = map_dict[position[0]]    
        direction = instructions_indexes[steps % len(instructions_indexes)]
        positions[i][0] = options[direction]
        steps += 1
        
        if position[0][2] == 'Z':
            print(last_step_count - steps)
            positions[i][1].append(steps - last_step_count)
            last_step_count = steps
            if len(positions[i][1]) > 50:
                z_found = True
        

for position in positions:
    print(position[1])
