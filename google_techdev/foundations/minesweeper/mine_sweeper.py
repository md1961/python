import random

class MineSweeper:

    def __init__(self, nx, ny):
        self.__board = Board(nx, ny)

    def put_mines(self, *coords):
        for x, y in coords:
            self.__board.put_mine(x, y)

    def put_random_mines(self, num):
        for i in range(num):
            self.__board.put_random_mine()

    def open(self, x, y):
        b = self.__board
        if b.is_open(x, y):
            return
        elif b.is_mine(x, y):
            print("BOOM!")
        else:
            b.open(x, y)

    def __str__(self):
        return str(self.__board)

class Board:

    OB = ' '
    MINE = '9'

    def __init__(self, nx, ny):
        self.__nx = nx
        self.__ny = ny
        self.__initialize()

    def __initialize(self):
        self.__cells = []
        for x in range(self.__nx + 2):
            if x in [0, self.__nx + 1]:
                row = [self.OB] * (self.__ny + 2)
            else:
                row = [self.OB] + ['0'] * self.__ny + [self.OB]
            self.__cells.append(row)

        self.__lids = []
        for x in range(self.__nx + 1):
            self.__lids.append([True] * (self.__ny + 1))

    def nx(self):
        return self.__nx

    def ny(self):
        return self.__ny

    def put_mine(self, x, y):
        self.__cells[x][y] = self.MINE
        for _x, _y in self.__adjacent_coordinates(x, y):
            if self.__cells[_x][_y] == self.MINE:
                continue
            self.__increment(_x, _y)

    def put_random_mine(self):
        while True:
            x = random.randrange(1, self.nx() + 1)
            y = random.randrange(1, self.ny() + 1)
            if not self.is_mine(x, y):
                break
        self.put_mine(x, y)

    def __adjacent_coordinates(self, x, y):
        return ((_x, _y) for _y in (y - 1, y, y + 1) for _x in (x - 1, x, x + 1) if _x != x or _y != y)

    def is_mine(self, x, y):
        return self.__cells[x][y] == self.MINE

    def is_open(self, x, y):
        return not self.__lids[x][y]

    def is_ob(self, x, y):
        return self.__cells[x][y] == self.OB

    def open(self, x, y):
        if self.is_ob(x, y) or self.is_open(x, y):
            return
        self.__lids[x][y] = False
        if self.__is_on_mine_edge(x, y):
            return
        for _x, _y in self.__adjacent_coordinates(x, y):
            self.open(_x, _y)

    def __is_on_mine_edge(self, x, y):
        return 1 <= int(self.__cells[x][y]) < 9

    def __increment(self, x, y):
        value = self.__cells[x][y]
        if value.isdigit():
            self.__cells[x][y] = str(int(value) + 1)

    def to_s(self):
        buffer = []
        for y in range(1, self.__ny + 1):
            buffer.append(' '.join([self.__cell_display(x, y) for x in range(1, self.__nx + 1)]))
        return "\n".join(buffer)

    def __cell_display(self, x, y):
        return '-' if self.__lids[x][y] else self.__cells[x][y]

    def __str__(self):
        return self.to_s()


if __name__ == '__main__':
    """
    ms = MineSweeper(5, 7)
    ms.put_mines((2, 4), (3, 6))
    ms.open(5, 1)

    ms = MineSweeper(10, 10)
    ms.put_mines((3, 3), (3, 8), (8, 3), (8, 8))
    ms.open(5, 5)
    """
    ms = MineSweeper(10, 10)
    ms.put_random_mines(5)
    x = random.randrange(10) + 1
    y = random.randrange(10) + 1
    ms.open(x, y)
    print(ms)
