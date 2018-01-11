class SubseqenceFinder:

    def __init__(self, str):
        self.__make_char_indexes(str)

    def __make_char_indexes(self, str):
        h = {}
        for index, char in enumerate(str):
            indexes = h.get(char, [])
            indexes.append(index)
            h[char] = indexes
        self.__char_indexes = h

    def is_subsequence(self, s):
        pos = 0
        for c in s:
            positions = [p for p in self.__char_indexes.get(c, []) if p >= pos]
            if len(positions) == 0:
                return False
            pos = positions[0] + 1
        return True

    def longest_subsequence(self, array_of_s):
        array_of_subseqs = filter(lambda s:self.is_subsequence(s), array_of_s)
        array_shortest_first = sorted(array_of_subseqs, key=lambda s:len(s))
        if len(array_shortest_first) == 0:
            return ''
        else:
            return array_shortest_first[-1]
