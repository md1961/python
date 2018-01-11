class SubseqenceFinder:

    def __init__(self, str):
        self.__str = str

    def is_subsequence(self, s):
        pos_start = 0
        for c in s:
            pos = self.__str.find(c, pos_start)
            if pos == -1:
                return False
            pos_start = pos + 1
        return True

    def longest_subsequence(self, array_of_s):
        array_of_subseqs = filter(lambda s:self.is_subsequence(s), array_of_s)
        array_shortest_first = sorted(array_of_subseqs, key=lambda s:len(s))
        if len(array_shortest_first) == 0:
            return ''
        else:
            return array_shortest_first[-1]
