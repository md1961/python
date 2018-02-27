import re

def index_of_close_paren(s):
    pos = 0
    while pos < len(s):
        pos = s.find(']', pos)
        if pos == -1:
            break
        s_before = s[:pos]
        if s_before.count('[') == s_before.count(']'):
            return pos
        pos += 1
    raise IndexError("No ']'")

def decomp(s):
    s_decomped = ''
    while s:
        m = re.match(r'\d+\[', s)
        if m:
            s = s[m.end():]
            n = int(m.group()[:-1])
            s_decomped += decomp(s) * n
            end = index_of_close_paren(s)
            s = s[end+1:]
        else:
            if s[0] == ']':
                break
            s_decomped += s[0]
            s = s[1:]
    return s_decomped


if __name__ == '__main__':
    import sys
    sys.path.insert(0, './codewars')
    import test

    test.assert_equals(decomp("10[a]"), "aaaaaaaaaa")
    test.assert_equals(decomp("3[abc]4[ab]c"), "abcabcabcababababc")
    test.assert_equals(decomp("2[3[a]b]c"), "aaabaaabc")
