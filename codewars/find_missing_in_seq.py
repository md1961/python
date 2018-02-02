def has_missing(sequence):
    size = len(sequence)
    if size <= 2:
        return False
    steps = list(map(lambda x: x[0] - x[1], zip(sequence[1:], sequence[:-1])))
    return len(set(steps)) > 1

def find_missing_sequentially(sequence):
    if not has_missing(sequence):
        return None
    steps = list(map(lambda x: x[0] - x[1], zip(sequence[1:], sequence[:-1])))
    is_ascending = sequence[-1] > sequence[0]
    bad_step = max(steps) if is_ascending else min(steps)
    index = next((i for i, step in enumerate(steps) if step == bad_step), None)
    return None if index is None else sum(sequence[index:index+2]) // 2

def find_missing(sequence):
    if not has_missing(sequence):
        return None
    # Cannot split into a sequence of two elments or less,
    # because the bad step will be lost.
    if len(sequence) <= 5:
        return find_missing_sequentially(sequence)
    i_mid = len(sequence) // 2
    sub1 = sequence[:i_mid]
    sub2 = sequence[i_mid:]
    if not has_missing(sub1) and not has_missing(sub2):
        return (sub1[-1] + sub2[0]) // 2
    elif has_missing(sub1):
        return find_missing(sub1)
    else:
        return find_missing(sub2)


if __name__ == '__main__':
    import random

    while True:
        n = random.choice([10, 100, 1000])
        start = random.randrange(-100, 10)
        step = random.randrange(1, 6)
        end = start + step * n
        seq = list(range(start, end, step))
        if random.randrange(2) == 1:
            seq.reverse()
            step = -step
        expected = random.choice(seq[1:-1])
        seq.remove(expected)
        actual = find_missing(seq)
        print("n = {}, start = {}, end = {}, step = {}".format(n, seq[0], seq[-1], step))
        print("{}: expected = {}, actual = {}".format(actual == expected, expected, actual))
        if actual != expected:
            break
