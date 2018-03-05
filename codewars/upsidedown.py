import re
from functools import reduce
import operator

def count_all_for(num_digits):
    n_for_mid = 1
    if num_digits % 2 == 1:
        n_for_mid = 3  # 0, 1, 8
        num_digits -= 1
    num_digits //= 2
    n_for_top = 4 if num_digits > 0 else 1  # 1, 8, 6, 9
    n_for_rest = max(5 ** (num_digits - 1), 1)  # 0, 1, 8, 6, 9
    return n_for_top * n_for_rest * n_for_mid
    n = 10 ** (num_digits - 1)
    #n = 10 ** num_digits - 1
    return count_for(n, is_greater=True)

def swap_digits_all(s, d1, d2):
    d1, d2 = map(str, (d1, d2))
    c_tmp = 'x'
    return s.replace(d1, c_tmp).replace(d2, d1).replace(c_tmp ,d2)

def is_upsidedown(n):
    s = str(n)
    if re.search(r'[23457]', s):
        return False
    s_rev = ''.join(reversed(s))
    return s == swap_digits_all(s_rev, 6, 9)

debug = 0
def count_for_same_num_digits_as(s_num, is_greater, allows_zero_at_top=False):

    if debug: print('"{} {}" ==> '.format('>' if is_greater else '<', s_num), end='')

    f_cmp_eq = operator.ge if is_greater else operator.le
    f_cmp_ne = operator.gt if is_greater else operator.lt
    f_count = lambda s_num, s_nums: len([n for n in map(int, s_nums) if f_cmp_eq(n, int(s_num))])
    f_choose = max if is_greater else min

    length = len(s_num)
    if length == 1:
        retval = f_count(s_num, ('0', '1', '8'))
    elif length == 2:
        nums = ('11', '69', '88', '96')
        if allows_zero_at_top:
            nums += ('00',)
        retval = f_count(s_num, nums)
    else:
        """
        1.0  ==>  a * 3 + s * 1    1 6 8 9
        1.1  ==>  a * 3 + s * 1    1 6 8 9   1
        1.2  ==>  a * 3 + s * 0      6 8 9   1
        6.8  ==>  a * 3 + s * 1      6 8 9   1
        6.9  ==>  a * 3 + s * 1      6 8 9   1 6
        7.0  ==>  a * 3 + s * 1        8 9   1 6
        8.7  ==>  a * 3 + s * 1        8 9   1 6
        8.8  ==>  a * 3 + s * 1        8 9   1 6 8
        8.9  ==>  a * 3 + s * 1          9   1 6 8
        9.5  ==>  a * 3 + s * 1          9   1 6 8
        9.6  ==>  a * 3 + s * 1          9   1 6 8 9
        9.7  ==>  a * 3 + s * 1              1 6 8 9
        """
        d1, d2 = s_num[0], s_num[-1]
        """
        if d1 == 6:
            d = d2 - (9 - 6)
        elif d1 == 9:
            d = d2 + (9 - 6)
        else:
            d = f_choose(d1, d2)
        """
        digits = ('1', '6', '8', '9')
        if allows_zero_at_top:
            digits += ('0',)
        count_d1 = f_count(d1, digits)
        if debug: print("(count_d1 = {})".format(count_d1))
        count = 0
        str_num_max_or_min = ('0' if is_greater else '9') * (length - 2)
        count_all_for_two_digit_less = count_for_same_num_digits_as(str_num_max_or_min, is_greater, allows_zero_at_top=True)
        if d1 not in digits:
            count += count_all_for_two_digit_less * count_d1
        else:
            if count_d1 > 1:
                count += count_all_for_two_digit_less * (count_d1 - 1)
            s_num_two_less = s_num[1:-1]
            count_sub_for_two_digit_less = count_for_same_num_digits_as(s_num_two_less, is_greater, allows_zero_at_top=True)
            count += count_sub_for_two_digit_less
            if d1 == '6':
                d2 = int(d2) - (9 - 6)
            elif d1 == '9':
                d2 = int(d2) + (9 - 6)
            if f_cmp_ne(int(d2), int(d1)) and is_upsidedown(s_num_two_less):
                #s_num_two_less == max_or_min_sub_str_num(len(s_num_two_less), is_max=is_greater) or s_num_two_less == '080':
                count -= 1
        retval = count
    if debug: print(retval)
    return retval

def max_or_min_sub_str_num(num_digits, is_max=True):
    if is_max:
        n_half = num_digits // 2
        mid = '8' if num_digits % 2 == 1 else ''
        return '9' * n_half + mid + '6' * n_half
    else:
        return '0' * num_digits

def first_half_and_mid_and_second_half_of(n):
    s = str(n)
    length = len(s)
    m1 = length // 2
    m2 = m1 + (1 if length % 2 == 1 else 0)
    half1 = s[:m1]
    mid = s[m1:m2]
    half2 = s[m2:]
    return half1, mid, half2

def upsidedown(x, y):
    count = count_for_same_num_digits_as(x, is_greater=True)
    count += count_for_same_num_digits_as(y, is_greater=False)
    for num_digits in range(len(x) + 1, len(y)):
        count += 4 * 5 ** (num_digits // 2 - 1) * (3 if num_digits % 2 == 1 else 1)
    return count


def upsidedown_brutally(x, y):
    count = 1 if is_upsidedown(x) else 0
    while True:
        x = int(x) + 1
        if int(x) > int(y):
            break
        if is_upsidedown(x):
            count += 1
    return count


if __name__ == '__main__':
    import sys
    sys.path.insert(0, './codewars')
    import test

    """
    debug = 1

    test.assert_equals(upsidedown('909080743', '1000000000'),312)
    quit()

    ('0','10'),
    ('6','25'),
    ('10','100'),
    ('100','1000'),

    args = (
        ('1234','12345'),
    )
    for arg in args:
        a1 = upsidedown(*arg)
        a2 = upsidedown_brutally(*arg)
        print("{}-{} : {} ({})".format(arg[0], arg[1], a1, a2))
    quit()

    for n in range(1, 11):
        actual = upsidedown('1' + '0' * (n - 1), '9' * n)
        print("{0:2}: {1} ({2})".format(n, count_all_for(n), actual))
    quit()

    count_for_same_num_digits_as('12345678900000000', is_greater=False)
    #                             11999999866666611
    #                             16000000000000091
    quit()
    """

    test.assert_equals(upsidedown('0','10'),3)
    test.assert_equals(upsidedown('6','25'),2)
    test.assert_equals(upsidedown('10','100'),4)
    test.assert_equals(upsidedown('100','1000'),12)
    test.assert_equals(upsidedown('100000','12345678900000000'),718650)
    test.assert_equals(upsidedown('10000000000','10000000000000000000000'),78120000)
    test.assert_equals(upsidedown('861813545615','9813815838784151548487'),74745418)
    test.assert_equals(upsidedown('5748392065435706','643572652056324089572278742'),2978125000)
    test.assert_equals(upsidedown('9090908074312','617239057843276275839275848'),2919867187)
