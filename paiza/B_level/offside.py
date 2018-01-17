team_ball, num_ball = input().split()
num_ball = int(num_ball)
pos_off = list(map(int, input().split()))
pos_def = list(map(int, input().split()))
if team_ball == 'B':
    pos_off, pos_def = pos_def, pos_off
    pos_off = list(map(lambda x: 110 - x, pos_off))
    pos_def = list(map(lambda x: 110 - x, pos_def))

h_pos_off = dict(enumerate([None] + pos_off))
h_pos_def = dict(enumerate([None] + pos_def))
del h_pos_off[0]
del h_pos_def[0]

nums_offside = [num for num, pos in h_pos_off.items() if
    pos >= 55 and
    pos > h_pos_off[num_ball] and
    pos > sorted(pos_def, reverse=True)[1]
]

print("\n".join(map(str, nums_offside)) if len(nums_offside) > 0 else 'None')
