input = open('input.txt', 'r')
lines = input.readlines()

spelled_numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
    ]

def find_first_number(line):
    partial_line = ''
    for char in line:
        if char.isdigit():
            return char
        partial_line += char
        for i, number in enumerate(spelled_numbers):
            if number in partial_line:
                return str(i+1)
    exit(1)
            
def find_second_number(line):
    partial_line = ''
    for char in reversed(line):
        if char.isdigit():
            return char
        partial_line = char + partial_line
        for i, number in enumerate(spelled_numbers):
            if number in partial_line:
                return str(i+1)
    exit(1)

accumulator = 0
     
for line in lines:
    number = find_first_number(line) + find_second_number(line)
    accumulator += int(number)
print(accumulator)
