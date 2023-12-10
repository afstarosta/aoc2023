input = open('input.txt', 'r')
lines = input.readlines()

accumulator = 0
for line in lines:
    number = ''
    for char in line:
        if char.isdigit():
            number += char
            break
    for char in reversed(line):
        if char.isdigit():
            number += char
            break
    accumulator += int(number)
print(accumulator)
