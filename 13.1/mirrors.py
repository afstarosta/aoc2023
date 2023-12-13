input = open('input.txt', 'r')
lines = input.readlines()

puzzles = [[]]
puzzle_counter = 0
for line in lines:
    if line == '\n':
        puzzle_counter += 1
        puzzles.append([])
    else:
        puzzles[puzzle_counter].append([i for i in line.replace('\n', '')])
    
def find_mirror_index(puzzle):
    found = False
    for i in range(len(puzzle)-1):
        if puzzle[i] == puzzle[i + 1]:
            if is_mirror(puzzle, i):
                return i + 1
    
    return 0

def is_mirror(puzzle, index):
    i = index
    j = index + 1
    while i >= 0 and j < len(puzzle):
        if puzzle[i] != puzzle[j]:
            return False
        i -= 1
        j += 1
    return True

acc = 0
for puzzle in puzzles:
    result = find_mirror_index(puzzle) * 100
    if result == 0:
        puzzle = [[puzzle[j][i] for j in range(len(puzzle))] for i in range(len(puzzle[0]))]
        result = find_mirror_index(puzzle)
    acc += result
print(acc)