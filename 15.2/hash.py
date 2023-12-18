input = open('input.txt', 'r')
lines = input.readlines()

boxes = {}
commands = lines[0].replace('\n', '').split(',')

def command_to_hash(command):
    value = 0
    for c in command:
        value += ord(c)
        value *= 17
        value = value % 256
    return value

def check_box(box):
    if not box in boxes:
        boxes[box] = {}

def process_equal_op(label, box, focal_length):
    check_box(box)
    boxes[box][label] = focal_length

def process_sub_op(label, box):
    check_box(box)
    if label in boxes[box]:
        del boxes[box][label]

for command in commands:
    label = ''
    box = -1
    focal_length = -1
    if '=' in command:
        label = command.split('=')[0]
        box = command_to_hash(label)
        focal_length = int(command.split('=')[1])
        process_equal_op(label, box, focal_length)
    
    else:
        label = command.split('-')[0]
        box = command_to_hash(label)
        process_sub_op(label, box)


acc = 0

for i, box in enumerate(boxes):
    for j, label in enumerate(boxes[box]):
        print((box + 1) * (j + 1) * boxes[box][label])
        acc += (box + 1) * (j + 1) * boxes[box][label]

print(acc)

print(boxes)