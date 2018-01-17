class OffsideJudge:

    def __init__(self, team_ball, num_ball):
        self.__team_ball = team_ball
        self.__num_ball = num_ball

    def set_positions(self, team, positions):
        if team == self.__team_ball:
            self.__h_pos_off = self.__positions_to_hash(positions)
        else:
            self.__h_pos_def = self.__positions_to_hash(positions)

    def __positions_to_hash(self, positions):
        h = dict(enumerate((None,) + positions))
        h.pop(0)
        return h

    def judge(self):
        if self.__team_ball == 'B':
            self.__reverse_coordinates(self.__h_pos_off)
            self.__reverse_coordinates(self.__h_pos_def)

        pos_def_2nd_last = sorted(tuple(self.__h_pos_def.values()), reverse=True)[1]
        nums_offside = (num for num, pos in self.__h_pos_off.items() if
            pos >= 55 and
            pos > self.__h_pos_off[self.__num_ball] and
            pos > pos_def_2nd_last
        )

        return tuple(nums_offside)

    def __reverse_coordinates(self, h_pos):
        for num, pos in h_pos.items():
            h_pos[num] = 110 - pos


if __name__ == '__main__':
    team_ball, num_ball = input().split()
    num_ball = int(num_ball)
    pos_a = tuple(map(int, input().split()))
    pos_b = tuple(map(int, input().split()))

    oj = OffsideJudge(team_ball, num_ball)
    oj.set_positions('A', pos_a)
    oj.set_positions('B', pos_b)
    nums_offside = oj.judge()
    print("\n".join(tuple(map(str, nums_offside))) if len(nums_offside) > 0 else 'None')
