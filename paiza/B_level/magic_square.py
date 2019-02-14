# coding: utf-8

class MagicSquare:

    __UNKNOWN = 0

    def __init__(self, rows):
        self.__rows = rows
        self.__calc_total_per_line()

    def solve(self):
        while not self.__is_solved():
            for row in rows:
                if self.__num_unknowns_in(row) == 1:
                    i_row = self.__index_of_first_unknown(row)
                    row[i_row] = self.__total_per_line - sum(row)
            for i_column in range(size):
                column = self.__column_at(i_column)
                if self.__num_unknowns_in(column) == 1:
                    i_row = self.__index_of_first_unknown(column)
                    rows[i_row][i_column] = self.__total_per_line - sum(column)

    def __str__(self):
        str_rows = [' '.join(map(str, row)) for row in self.__rows]
        return "\n".join(str_rows)

    # 以下はプライベート・メソッド

    def __calc_total_per_line(self):
        size = len(self.__rows)
        max_number = size * size
        self.__total_per_line = (1 + max_number) * max_number // 2 // size
        # // は整数除算

    def __num_unknowns_in(self, numbers):
        return numbers.count(self.__UNKNOWN)

    def __index_of_first_unknown(self, numbers):
        return numbers.index(self.__UNKNOWN)

    def __column_at(self, i_column):
        cols = []
        for row in self.__rows:
            cols.append(row[i_column])
        return cols

    def __is_solved(self):
        return sum([self.__num_unknowns_in(row) for row in self.__rows]) == 0


if __name__ == '__main__':
    size = int(input())
    rows = []
    for _ in range(size):
        row = list(map(int, input().split()))
        rows.append(row)

    ms = MagicSquare(rows)
    ms.solve()
    print(ms)
