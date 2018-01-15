from random import choice
from collections import defaultdict

class Lexicon:

    def get_word_count(self):
        return len(WORDS)

    def get_word(self, index):
        return WORDS[index]

    def pick_word(self):
        return choice(self.WORDS)

    WORDS = tuple(map(lambda s: s.upper(), [
        'BUOY', 'COMPUTER', 'CONNOISSEUR', 'DEHYDRATE', 'FUZZY',
        'HUBBUB', 'KEYHOLE', 'QUAGMIRE', 'SLITHER', 'ZIRCON',

        'enumerate', 'hangman', 'gallow', 'python', 'java',
        'language', 'choice', 'ruby', 'visual', 'railway',
        'sequence', 'write', 'tuple', 'foxy', 'joker',
    ]))

if __name__ == '__main__':
    h_counts_by_length = defaultdict(int)
    h_char_counts = defaultdict(int)
    for word in Lexicon.WORDS:
        h_counts_by_length[len(word)] += 1
        for ch in word:
            h_char_counts[ch] += 1
    for length, count in h_counts_by_length.items():
        print("{0:>2}:{1:>3}".format(length, count))
    print()
    for n in range(ord('A'), ord('Z') + 1):
        ch = chr(n)
        print("{0}:{1:>3}".format(ch, h_char_counts[ch]))
