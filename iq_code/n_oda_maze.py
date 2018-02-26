INPUT = """*oxxooo
oooooxo
oxxxxoo
oxo*xox
oooxxox
xxoooox
oooxxoo"""
INPUT = """*xxxooo
oooooxo
oxxxxoo
oxo*xox
oxoxxox
xxoooox
oooxxoo"""

inputs = INPUT.split('\n')

inputs = []
for _ in range(7):
    inputs.append(input())

routes = [[None] * (7 + 2) for _ in range(7 + 2)]
for y in range(1, 7 + 1):
    for x in range(1, 7 + 1):
        if inputs[y - 1][x - 1] != 'x':
            routes[y][x] = 0

OFFSETS = ((1, 0), (0, 1), (-1, 0), (0, -1))
cursors = [(1, 1)]
while cursors:
    if 0 < routes[4][4] <= 15:
        break
    x, y = cursors.pop()
    for dx, dy in OFFSETS:
        cur = routes[y][x]
        adj = routes[y + dy][x + dx]
        if adj is not None and (adj == 0 or cur + 1 < adj):
            routes[y + dy][x + dx] = cur + 1
            cursors.append((x + dx, y + dy))
    routes[1][1] = -1

print('yes' if 0 < routes[4][4] <= 15 else 'no')

for y in range(1, 7 + 1):
    for x in range(1, 7 + 1):
        r = routes[y][x]
        print('XX ' if r is None else '{0:2} '.format(r), end='')
    print()
