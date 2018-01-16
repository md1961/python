class Hanoi:

    NUM_STICKS = 3
    START = 0
    GOAL  = 2

    def __init__(self, num_plates):
        self.sticks = [[] for i in range(self.NUM_STICKS)]
        self.sticks[self.START] = [i + 1 for i in reversed(range(num_plates))]

    def move(self, num_moves):
        self.num_moves = num_moves
        try:
            self.__move_part(self.START, self.GOAL, len(self.sticks[self.START]))
        except StopIteration:
            pass

    def __move_part(self, i_from, i_to, num_plates):
        if num_plates == 1:
            plate = self.sticks[i_from].pop()
            self.sticks[i_to].append(plate)
            self.num_moves -= 1
            if self.num_moves == 0:
                raise StopIteration
        else:
            i_work = 3 - sum([i_from, i_to])
            self.__move_part(i_from, i_work, num_plates - 1)
            self.__move_part(i_from, i_to  , 1)
            self.__move_part(i_work, i_to  , num_plates - 1)

    def __str__(self):
        return "\n".join(map(self.__stick_to_str, self.sticks))

    def __stick_to_str(self, stick):
        if len(stick) == 0:
            return '-'
        else:
            return ' '.join(map(str, stick))

if __name__ == '__main__':
    num_plates, num_moves = map(int, input().split())
    hanoi = Hanoi(num_plates)
    hanoi.move(num_moves)
    print(hanoi)
