from random import choice

class Lexicon:

    def get_word_count(self):
        return len(WORDS)

    def get_word(self, index):
        return WORDS[index]

    def pick_word(self):
        return choice(self.WORDS)

    WORDS = [
        "BUOY", "COMPUTER", "CONNOISSEUR", "DEHYDRATE", "FUZZY",
        "HUBBUB", "KEYHOLE", "QUAGMIRE", "SLITHER", "ZIRCON",
        "ENUMERATE"
    ]
