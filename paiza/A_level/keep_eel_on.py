def reverse_direction(wing):
    return 'R' if wing == 'L' else 'L'

def directions_for(wing, offset, d_moves, next_d):
    d = d_moves[0]
    if len(d_moves) == 1:
        if d >= len_wing - (len_wing * 2 - next_d) - offset and d <= len_wing - offset:
            return wing
        elif d >= len_wing - (len_wing * 2 - next_d) + offset + 1 and d <= len_wing + offset + 1:
            return reverse_direction(wing)
        return '?'
    elif d_moves[0] > len_wing - offset:
        dir = reverse_direction(wing)
        offset = offset - d_moves[0]
        if offset < 0:
            offset = -offset
            wing = dir
        return dir + directions_for(wing, offset, d_moves[1::], next_d)
    else:
        result = wing + directions_for(wing, offset + d, d_moves[1::], next_d)
        if result[-1] == '?':
            opp_wing = reverse_direction(wing) 
            offset = offset - d
            if offset < 0:
                offset = -offset
                wing = opp_wing
            result = opp_wing + directions_for(wing, offset, d_moves[1::], next_d)
        return result


len_wing, n_times = map(int, input().split())
d_moves = [int(input()) for i in range(n_times)]

d_moves_parted = []
buffer = []
for d in d_moves:
    if d > len_wing:
        if len(buffer) > 0:
            d_moves_parted.append(buffer)
            buffer = []
        d_moves_parted.append(d)
    else:
        buffer.append(d)
if len(buffer) > 0:
    d_moves_parted.append(buffer)

directions = ""
wing = 'R'
offset = 0
for i, d in enumerate(d_moves_parted):
    if isinstance(d, list):
        if i == len(d_moves_parted) - 1:
            next_d = 0
        else:
            next_d = d_moves_parted[i + 1]
        directions += directions_for(wing, offset, d, next_d)
    else:
        wing = reverse_direction(wing)
        offset = d - offset
        directions += wing

print(directions)
