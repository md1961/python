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
    elif n_fingers in {1, 3}:
        max_w = None
    elif n_fingers in {2, 4}:
        if hands.count('P') >= 1:
            m = max_win(delete_hand(hands, 'P'), n_fingers - 2)
            max_w = add_with_none(1, m)
        else:
            m1 = m2 = m3 = m4 = 0
            if hands.count('G') >= 1:
                m1 = max_win(delete_hand(hands, 'G'), n_fingers - 2)
                m2 = max_win(delete_hand(hands, 'G'), n_fingers)
            if hands.count('C') >= 1:
                m3 = max_win(delete_hand(hands, 'C'), n_fingers - 2)
                m4 = max_win(delete_hand(hands, 'C'), n_fingers)
            max_w = max_with_none(m1, m2, m3, m4)
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
            #print((hands, n_fingers))
            m = max_win(delete_hand(hands, 'C'), n_fingers)
            max_w = add_with_none(1, m)
    max_wins[(normalize(hands), n_fingers)] = max_w
    return max_w

def delete_hand(s, c):
    l = list(s)
    l.remove(c)
    return ''.join(l)

def normalize(hands):
    return ''.join([h + str(hands.count(h)) for h in ('G', 'C', 'P')])

def max_with_none(*nums):
    if None in nums and len(set(nums)) == 1:
        return None
    else:
        return max([n for n in nums if n is not None])

def add_with_none(n1, n2):
    if None in (n1, n2):
        return None
    else:
        return n1 + n2

print(max_win(opp_hands, total_fingers))
