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
    

def compare_with_smudge(a, b):
    if a == b:
        return True, False
    diff = sum ( a[i] != b[i] for i in range(len(a)) )
    if diff == 1:
        return True, True
    return False, False

def find_mirror_index_with_smudge(puzzle):
    found = False
    for i in range(len(puzzle)-1):
        equal, smudge = compare_with_smudge(puzzle[i], puzzle[i + 1])
        if equal:
            valid_mirror, smudge = is_mirror_with_smudge(puzzle, i, smudge)
            if valid_mirror and smudge:
                print(puzzle[i])
                return i + 1
    
    return 0

def is_mirror_with_smudge(puzzle, index, smudge):
    i = index - 1
    j = index + 2
    while i >= 0 and j < len(puzzle):
        if smudge:
            if puzzle[i] != puzzle[j]:
                return False, smudge
        else:
            equal, smudge = compare_with_smudge(puzzle[i], puzzle[j])
            if not(equal):
                return False, smudge
        i -= 1
        j += 1
    return True, smudge

acc = 0
for puzzle in puzzles:
    result = find_mirror_index_with_smudge(puzzle) * 100
    if result == 0:
        puzzle = [[puzzle[j][i] for j in range(len(puzzle))] for i in range(len(puzzle[0]))]
        result = find_mirror_index_with_smudge(puzzle)
    acc += result
print(acc)