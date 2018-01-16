class MineSweeper:
    pass

class Board:

    OB = ' '
    MINE = '9'

    def __init__(self, nx, ny):
        self.__nx = nx
        self.__ny = ny
        self.__initialize()

    def __initialize(self):
        self.__cells = []
        for y in range(self.__ny + 2):
            if y in [0, self.__ny + 1]:
                row = [self.OB] * (self.__nx + 2)
            else:
                row = [self.OB] + ['0'] * self.__nx + [self.OB]
            self.__cells.append(row)

    def put_mine(self, x, y):
        self.__cells[y][x] = self.MINE
        for _x, _y in [(_x, _y) for _y in (y - 1, y, y + 1) for _x in (x - 1, x, x + 1)]:
            if _x == x and _y == y:
                continue
            if self.__cells[_y][_x] == self.MINE:
                continue
            self.__increment(_x, _y)

    def __increment(self, x, y):
        value = self.__cells[y][x]
        if value.isdigit():
            self.__cells[y][x] = str(int(value) + 1)

    def to_s(self):
        buffer = []
        for y in range(1, self.__ny + 1):
            buffer.append(' '.join([self.__cells[y][x] for x in range(1, self.__nx + 1)]))
        return "\n".join(buffer)

    def __str__(self):
        return self.to_s()


if __name__ == '__main__':
    b = Board(5, 7)
    b.put_mine(2, 4)
    b.put_mine(3, 6)
    print(b)
