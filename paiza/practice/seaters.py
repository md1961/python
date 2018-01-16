# coding: utf-8

class RoundTable:

    def __init__(self, n_seats):
        self.seats = [0] * (n_seats + 1)  # seast[0] unused.

    def num_seated(self):
        return sum(self.seats)

    def seat(self, n_seaters, index_seat_start):
        if self.__is_empty(n_seaters, index_seat_start):
            self.__mark(n_seaters, index_seat_start)

    def __is_empty(self, n_seaters, index_seat_start):
        index_end = index_seat_start + n_seaters
        return sum((self.seats + self.seats[1:])[index_seat_start:index_end]) == 0

    def __mark(self, n_seaters, index_seat_start):
        index_end = index_seat_start + n_seaters
        if index_end > len(self.seats) + 1:
            n_out_of_range = index_end - len(self.seats)
            self.__mark(n_out_of_range, 1)
            n_seaters -= n_out_of_range
            index_end = len(self.seats) + 1
        self.seats[index_seat_start:index_end] = [1] * n_seaters

if __name__ == '__main__':
    n_seats, n_groups = map(int, input().split())
    rt = RoundTable(n_seats)

    for i in range(n_groups):
        n_seaters, index_seat_start = map(int, input().split())
        rt.seat(n_seaters, index_seat_start)

    print(rt.num_seated())
