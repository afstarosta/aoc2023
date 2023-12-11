input = open('input.txt', 'r')
map = input.readlines()

directions = {
    'S': [1, 0], 
    'N': [-1, 0], 
    'E': [0, 1], 
    'W': [0, -1]
    }

direction_inversion = {
    'E': 'W',
    'W': 'E',
    'S': 'N',
    'N': 'S'
}


start_marker = 'S'

pipe_connections = {
    '|': {'N': 'S', 'S': 'N'},
    '-': {'W': 'E', 'E': 'W' },
    'L': {'N': 'E', 'E': 'N' },
    'J': {'N': 'W', 'W': 'N' },
    '7': {'S': 'W', 'W': 'S' },
    'F': {'S': 'E', 'E': 'S' },
}

starting_position = []
for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == start_marker:
            starting_position = [i, j]
            break
    if starting_position != []:
        break


def get_valid_neighbors(position, map):
    neighbors = []
    for direction in ['S', 'W', 'E', 'N']:
        transformation = directions[direction]
        target = [position[0] + transformation[0], position[1] + transformation[1]]
        if 0 <= target[0] <= len(map) -1 and 0 <= target[1] <= len(map[target[0]]):
            pipe_type = map[target[0]][target[1]]
            if pipe_type in pipe_connections and direction_inversion[direction] in pipe_connections[pipe_type]:
                neighbors.append([direction, target, pipe_type])
    return neighbors

print(starting_position)
valid_neighbors = get_valid_neighbors(starting_position, map)

current_position = valid_neighbors[0][1]
last_direction = valid_neighbors[0][0]
last_pipe_type = valid_neighbors[0][2]

steps = 1
print(starting_position)

while current_position != starting_position:
    direction_inverted = direction_inversion[last_direction]
    next_direction = pipe_connections[last_pipe_type][direction_inverted]
    transformation = directions[next_direction]
    target = [current_position[0] + transformation[0], current_position[1] + transformation[1]]
    print(f"{last_direction=}")
    print(f"{direction_inverted=}")
    print(f"{next_direction=}")
    print(f"{target=}")

    last_pipe_type = map[target[0]][target[1]]
    last_direction = next_direction
    
    steps += 1
    current_position = target

print()
for line in map:
    print(line.replace('\n', ''))

print(steps)
print(steps // 2)
