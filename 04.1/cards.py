input = open('input.txt', 'r')
lines = input.readlines()

accumulator = 0
for line in lines:
    line = line.replace('  ', ' ')
    line_accumulator = 0
    winning_numbers = list(map(int,line.split(':')[1].split('|')[0].strip().split(' ')))
    played_numbers = list(map(int,line.split(':')[1].split('|')[1].strip().split(' ')))

    for number in played_numbers:
        if number in winning_numbers:
            line_accumulator = 1 if (line_accumulator == 0) else line_accumulator * 2
    
    accumulator += line_accumulator
print(accumulator)
