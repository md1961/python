from lexicon import Lexicon

MAX_TRIES = 8

answer = Lexicon().pick_word()
display = '-' * len(answer)
print(display)

n_tries = MAX_TRIES
guesses = []
while n_tries > 0:
    while True:
        print('Your guess(' + str(n_tries) + ' left): ', end='')
        ch = input().upper()
        if len(ch) == 1 and ch.isalpha() and ch not in guesses:
            break
    guesses.append(ch)
    if ch not in answer:
        print("There are no " + ch + "'s")
    else:
        pos_s = list(filter(lambda x: x >= 0, [i if c == ch else -1 for i, c in enumerate(answer)]))
        display = ''.join([ch if i in pos_s else c for i, c in enumerate(display)])
        if '-' not in display:
            break
    print(display)
    n_tries -= 1
print("answer is '" + answer + "'")
