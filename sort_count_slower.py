n_max = int(input())
nums = [None] + list(map(int, input().split()))

num_index = [None] + [nums.index(n) for n in range(1, n_max + 1)]

count = 0
for i in range(1, n_max + 1):
    num = nums[i]
    if num == i:
        continue
    elif num < i:
        count += 1
        continue
    elif nums[num] > num:
        count += 1
        continue

    j = num_index[i]
    while True:
        if j == nums[i]:
            break
        elif j > nums[i]:
            count += 1
            break
        j = num_index[j]

print(count)
