input = open('input.txt', 'r')
lines = input.readlines()

accumulator = 0
cards_multiplication = []

for line in lines:
    line = line.replace('  ', ' ')
    line_accumulator = 0
    winning_numbers = list(map(int,line.split(':')[1].split('|')[0].strip().split(' ')))
    played_numbers = list(map(int,line.split(':')[1].split('|')[1].strip().split(' ')))

    for number in played_numbers:
        if number in winning_numbers:
            line_accumulator += 1
    
    cards_multiplication.append([1, line_accumulator])

for index, multiplication in enumerate(cards_multiplication):
    for i in range(0, multiplication[0]):
        for j in range(multiplication[1]):
            cards_multiplication[index + j + 1][0] += 1

for multiplication in cards_multiplication:
    accumulator += multiplication[0]

print(accumulator)

