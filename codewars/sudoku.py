import math

def sudoku(problem):
    size = len(problem)
    size_sqr = int(math.sqrt(size))

    def coords_in_row_at(i_row):
        return [(i_row, i_col) for i_col in range(size)]

    def coords_in_col_at(i_col):
        return [(i_row, i_col) for i_row in range(size)]

    def coords_in_sqr_at(index):
        index_row = index // size_sqr
        index_col = index %  size_sqr
        i_row0 = index_row * size_sqr
        i_row1 = i_row0 + size_sqr
        i_col0 = index_col * size_sqr
        i_col1 = i_col0 + size_sqr
        return [(i_row, i_col) for i_row in range(i_row0, i_row1) for i_col in range(i_col0, i_col1)]

    def is_solved():
        for row in problem:
            for value in row:
                if value == 0:
                    return False
        return True

    mat_possibles = [[[v + 1 for v in range(size)] for _x in range(size)] for _y in range(size)]
    for i_row in range(size):
        for i_col in range(size):
            if problem[i_row][i_col] > 0:
                mat_possibles[i_row][i_col] = []

    while not is_solved():
        for f_coords in (coords_in_row_at, coords_in_col_at, coords_in_sqr_at):
            for index in range(size):
                coords = f_coords(index)
                for i_row, i_col in coords:
                    value = problem[i_row][i_col]
                    if value == 0:
                        continue
                    for i_r, i_c in coords:
                        possibles = mat_possibles[i_r][i_c]
                        if value in possibles:
                            possibles.remove(value)
                        if len(possibles) == 1:
                            problem[i_r][i_c] = possibles.pop()

    return problem

def print_matrix(mat):
    for row in mat:
        print(row)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, './codewars')
    import test

    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    expected = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]
    test.assert_equals(sudoku(puzzle), expected)
