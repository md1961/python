import sys, random

argv = sys.argv
if (len(argv) != 2):
    print('Specify number of times to iterate')
    quit()

n_times = int(argv[1])
total = 0
for i in range(n_times):
    d1 = random.random()
    d2 = random.random()
    total += abs(d2 - d1)

print(total / n_times)
