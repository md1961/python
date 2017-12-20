# +
# +0-
# +0-0+1-
# +0-0+1-0+0-1+1-

n = int(input())
s = '+'
for i in range(n):
    t = ''
    for c in s:
        if c == '+':
            t += '+0-'
        elif c == '-':
            t += '+1-'
        else:
            t += c
    s = t
print(''.join(list(filter(lambda c: c in {'0', '1'}, s))))
