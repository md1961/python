"""
2 3
..#
...
""

import sys, random

n_blocks = int(sys.argv[1]) if len(sys.argv) >= 2 else 9
nx, ny = (9, 9)
coords_blocks = []
while len(coords_blocks) < n_blocks:
    x = random.randrange(nx)
    y = random.randrange(ny)
    if (x, y) in ((0, 0), (nx - 1, ny - 1)):
        continue
    elif (x, y) not in coords_blocks:
        coords_blocks.append((x, y))

for y in range(ny):
    print(''.join(['#' if (x, y) in coords_blocks else '.' for x in range(nx)]))

quit()
"""

def print_turns(turns):
    print("    ", end='')
    for y in range(len(turns[0])):
        print("{0:>2}  ".format(y), end='')
    print()
    print('-' * (3 + 4 * len(turns[0])))
    for x, row in enumerate(turns):
        print("{0:>2}: ".format(x), end='')
        for cell in row:
            if cell is None:
                print(" N  ", end='')
            else:
                s = ','.join(map(lambda e: 'N' if e == BLOCK else str(e), cell)) + ' '
                print(s, end='')
        print()

nx, ny = 9, 9
paths = tuple(map(list, [
    ".#.#.....",
    ".....#...",
    "....#..#.",
    "..##.....",
    "......#..",
    "#..#.#..#",
    ".##..#...",
    "......#.#",
    "......#..",
]))

#nx, ny = map(int, input().split())
#paths = tuple([tuple(input()) for x in range(nx)])

BLOCK = 99999999

turns = [[None] * ny for x in range(nx)]

x = 0
blocked = False
for y in range(ny):
    if paths[x][y] == '#' or blocked:
        turns[x][y] = (BLOCK, BLOCK)
        blocked = True
    else:
        turns[x][y] = (BLOCK, 0)
y = 0
blocked = False
for x in range(nx):
    if paths[x][y] == '#' or blocked:
        turns[x][y] = (BLOCK, BLOCK)
        blocked = True
    else:
        turns[x][y] = (0, BLOCK)
turns[0][0] = [0, 0]

for x in range(1, nx):
    for y in range(1, ny):
        cell_above = turns[x - 1][y]
        if paths[x][y] == '#':
            turns[x][y] = (BLOCK, BLOCK)
        else:
            if cell_above == (BLOCK, BLOCK):
                downward = BLOCK
            else:
                downward = min(cell_above[0], cell_above[1] + 1)
            cell_left = turns[x][y - 1]
            if cell_left == (BLOCK, BLOCK):
                rightward = BLOCK
            else:
                rightward = min(cell_left[0] + 1, cell_left[1])
            turns[x][y] = [downward, rightward]

#print(min(turns[-1][-1]))
print_turns(turns)
