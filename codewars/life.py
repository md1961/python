def add_dead_boundaries_to(cells):
    ny = len(cells)
    for x in (0, 1):
        if sum(cells[y][x] for y in range(ny)) > 0:
            for y in range(ny):
                cells[y].insert(0, 0)
    for x in (-1, -2):
        if sum(cells[y][x] for y in range(ny)) > 0:
            for y in range(ny):
                cells[y].append(0)
    nx = len(cells[0])
    for y in (0, 1):
        if sum(cells[y]) > 0:
            cells.insert(0, [0] * nx)
    for y in (-1, -2):
        if sum(cells[y]) > 0:
            cells.append([0] * nx)

def remove_dead_boundaries_from(cells):
    ny = len(cells)
    while sum(cells[y][0] for y in range(ny)) == 0:
        for y in range(ny):
            cells[y].pop(0)
    while sum(cells[y][-1] for y in range(ny)) == 0:
        for y in range(ny):
            cells[y].pop(-1)
    while sum(cells[0]) == 0:
        cells.pop(0)
    while sum(cells[-1]) == 0:
        cells.pop(-1)

def neighbor_count(cells, x, y):
    if x == 0 or x == len(cells[0]) - 1:
        raise IndexError("x ({}) is at boundary".format(x))
    if y == 0 or y == len(cells) - 1:
        raise IndexError("y ({}) is at boundary".format(y))
    neighbors_and_self = [cells[_y][_x] for _x in range(x - 1, x + 2) for _y in range(y - 1, y + 2)]
    return sum(neighbors_and_self) - cells[y][x]

def next_gen(cells):
    next_cells = [[0] * len(cells[0]) for _ in range(len(cells))]
    for y in range(1, len(cells) - 1):
        for x in range(1, len(cells[0]) - 1):
            count = neighbor_count(cells, x, y)
            if count == 3 or (count == 2 and cells[y][x] == 1):
                next_cells[y][x] = 1
            else:
                next_cells[y][x] = 0
    return next_cells

def get_generation(initial_cells, generations):
    """
    - Any live cell with fewer than 2 live neighbours dies.
    - Any live cell with more than 3 live neighbours dies.
    - Any live cell with 2 or 3 live neighbours lives on.
    - Any dead cell with exactly 3 live neighbours becomes a live cell.
    """
    cells = [row[:] for row in initial_cells]
    for _ in range(generations):
        add_dead_boundaries_to(cells)
        cells = next_gen(cells)
    remove_dead_boundaries_from(cells)
    return cells


if __name__ == '__main__':
    import sys
    sys.path.insert(0, './codewars')
    import test

    def print_cells(cells):
        for row in cells:
            print(' '.join(map(str, row)))

    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end   = [[0,1,0],
             [0,0,1],
             [1,1,1]]
    orig_start = [row[:] for row in start]
    actual = get_generation(start, 1)
    test.assert_equals(actual, end)
    test.assert_equals(start, orig_start)

    quit()

    cells = start
    for _ in range(10):
        cells = get_generation(cells, 1)
        print_cells(cells)
        print()
