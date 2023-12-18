input = open('input.txt', 'r')
lines = input.readlines()

commands = lines[0].replace('\n', '').split(',')

def command_to_hash(command):
    value = 0
    for c in command:
        value += ord(c)
        value *= 17
        value = value % 256
    return value

acc = 0
for c in commands:
    acc += command_to_hash(c)

print(acc)