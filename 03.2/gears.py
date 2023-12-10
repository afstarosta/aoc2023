directions = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]

def check_for_gear(i, j, lines):
    for direction in directions:
        coordinate = [i + direction[0], j + direction[1]]
        if coordinate[0] < len(lines) and coordinate[1] < len(lines[coordinate[0]]):
            char = lines[coordinate[0]][coordinate[1]]
            if char == '*':
                return True, coordinate
    return False, []


input = open('input.txt', 'r')
lines = input.readlines()

gears = {}

for i, line in enumerate(lines):
    current_number = ''
    gear_coordinates = []
    is_valid_number = False
    for j, char in enumerate(line):
        if char.isdigit():
            current_number += char
            if not(is_valid_number):
                is_valid_number, gear_coordinates = check_for_gear(i, j, lines)
        else:
            if current_number != '' and is_valid_number:
                key = ', '.join(map(str, gear_coordinates))
                if key in gears:
                    gears[key].append(int(current_number))
                else:
                    gears[key] = [int(current_number)]
            current_number = ''
            is_valid_number = False

accumulator = 0
for coord, numbers in gears.items():
    if len(numbers) == 2:
        accumulator += numbers[0] * numbers[1]
print(accumulator)
    

