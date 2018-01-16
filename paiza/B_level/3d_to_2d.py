max_x, max_y, max_z = list(map(int, input().split()))

cells = []
for x in range(max_x + 1):
    rows = []
    for y in range(max_y + 1):
        rows.append(['.'] * (max_z + 1))
    cells.append(rows)

for z in range(1, max_z + 1):
    for x in range(1, max_x + 1):
        for y, c in enumerate(input()):
            cells[x][y + 1][z] = c
    input()

for z in range(max_z, 0, -1):
    for y in range(1, max_y + 1):
        c = '#' in ''.join([cells[x][y][z] for x in range(1, max_x + 1)])
        print('#' if c else '.', end='')
    print()
