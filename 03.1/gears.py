directions = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]

def check_for_symbols(i, j, lines):
    for direction in directions:
        coordinate = [i + direction[0], j + direction[1]]
        if coordinate[0] < len(lines) and coordinate[1] < len(lines[coordinate[0]]):
            char = lines[coordinate[0]][coordinate[1]]
            if not(char.isdigit()) and (char != '.') and (char != '\n'):
                print(char)
                return True
    return False


input = open('input.txt', 'r')
lines = input.readlines()

numbers = []
accumulator = 0

for i, line in enumerate(lines):
    current_number = ''
    is_valid_number = False
    for j, char in enumerate(line):
        if char.isdigit():
            current_number += char
            if not(is_valid_number):
                is_valid_number = check_for_symbols(i, j, lines)
        else:
            if current_number != '' and is_valid_number:
                print(current_number)
                accumulator += int(current_number)
            current_number = ''
            is_valid_number = False

print(accumulator)
