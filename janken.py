num_plays, total_fingers = map(int, input().split())
opp_hands = input()

#total_for_5 = opp_hands.count('G')
#total_for_2 = opp_hands.count('P')

# count_for_5 * 5 + count_for_2 * 2 = total_fingers
# count_for_5 <= total_for_5
# count_for_2 <= total_for_2
# count_for_5 + count_for_2  ==>  max

max_wins = {}

def max_win(hands, n_fingers):
    max_w = max_wins.get((normalize(hands), n_fingers))
    if max_w is not None:
        return max_w
    elif hands == '':
        if n_fingers == 0:
            max_w = 0
        else:
            max_w = None
    elif n_fingers == 0:
        max_w = hands.count('C')
    elif n_fingers > len(hands) * 5:
        return None
    elif n_fingers in {1, 3}:
        max_w = None
    elif n_fingers in {2, 4}:
        if hands.count('P') >= 1:
            m = max_win(delete_hand(hands, 'P'), n_fingers - 2)
            max_w = add_with_none(1, m)
        else:
            m1 = m2 = None
            if hands.count('G') >= 1:
                m3 = max_win(delete_hand(hands, 'G'), n_fingers - 2)
                m4 = max_win(delete_hand(hands, 'G'), n_fingers)
                m1 = max_with_none(m3, m4)
            if hands.count('C') >= 1:
                m5 = max_win(delete_hand(hands, 'C'), n_fingers - 2)
                m6 = max_win(delete_hand(hands, 'C'), n_fingers)
                m2 = max_with_none(m5, m6)
            max_w = max_with_none(m1, m2)
    else:
        if hands.count('G') >= 1 and hands.count('P') >= 1:
            m1 = max_win(delete_hand(hands, 'G'), n_fingers - 5)
            m2 = max_win(delete_hand(hands, 'P'), n_fingers - 2)
            max_w = add_with_none(1, max_with_none(m1, m2))
            m3 = max_win(delete_hand(hands, 'G'), n_fingers)
            m4 = max_win(delete_hand(hands, 'P'), n_fingers)
            max_w = max_with_none(max_w, m3, m4)
        elif hands.count('G') >= 1:
            m1 = max_win(delete_hand(hands, 'G'), n_fingers - 5)
            m2 = max_win(delete_hand(hands, 'G'), n_fingers - 2)
            m3 = max_win(delete_hand(hands, 'G'), n_fingers)
            max_w = max_with_none(add_with_none(1, m1), m2, m3)
        elif hands.count('P') >= 1:
            m1 = max_win(delete_hand(hands, 'P'), n_fingers - 2)
            m2 = max_win(delete_hand(hands, 'P'), n_fingers - 5)
            m3 = max_win(delete_hand(hands, 'P'), n_fingers)
            max_w = max_with_none(add_with_none(1, m1), m2, m3)
        else:
            m1 = max_win(delete_hand(hands, 'C'), n_fingers)
            m2 = max_win(delete_hand(hands, 'C'), n_fingers - 2)
            m3 = max_win(delete_hand(hands, 'C'), n_fingers - 5)
            max_w = max_with_none(add_with_none(1, m1), m2, m3)
    max_wins[(normalize(hands), n_fingers)] = max_w
    return max_w

def delete_hand(s, c, count=1):
    l = list(s)
    for i in range(count):
        l.remove(c)
    return ''.join(l)

def normalize(hands):
    return ''.join([h + str(hands.count(h)) for h in ('G', 'C', 'P')])

def max_with_none(*nums):
    if set(nums) == {None}:
        return None
    else:
        return max([n for n in nums if n is not None])

def add_with_none(n1, n2):
    if None in (n1, n2):
        return None
    else:
        return n1 + n2

answer = None
count_offset_for_0 = 0
count_offset_for_2 = 0
count_offset_for_5 = 0
prev_args = None
while True:
    max_w = 0
    hands = opp_hands
    n_fingers = total_fingers

    count = max(hands.count('C') - count_offset_for_0, 0)
    hands = delete_hand(hands, 'C', count)
    max_w += count

    count = max(min(hands.count('P'), int(n_fingers / 2)) - count_offset_for_2, 0)
    hands = delete_hand(hands, 'P', count)
    n_fingers -= count * 2
    max_w += count

    count = max(min(hands.count('G'), int(n_fingers / 5)) - count_offset_for_5, 0)
    hands = delete_hand(hands, 'G', count)
    n_fingers -= count * 5
    max_w += count

    if n_fingers < 0:
        break
    m = None
    if (hands, n_fingers) != prev_args:
        print((max_w, (hands, n_fingers), round(n_fingers / (len(hands) or 1), 3)))
        m = max_win(hands, n_fingers)
        prev_args = (hands, n_fingers)

    if m is not None:
        answer = max_w + m
        break

    if count_offset_for_0 == count_offset_for_2 == count_offset_for_5:
        count_offset_for_0 += 1
    elif count_offset_for_2 == count_offset_for_5:
        count_offset_for_2 += 1
    else:
        count_offset_for_5 += 1

    if count_offset_for_0 > 10 and count_offset_for_2 > 10 and count_offset_for_5 > 10:
        break

print(answer)
