n_max = int(input())
nums = [None] + list(map(int, input().split()))

num_index = dict([(n, i) for i, n in enumerate(nums)])

count = 0
for i in range(1, n_max + 1):
    if nums[i] == i:
        continue
    j = num_index[i]
    nums[i], nums[j] = nums[j], nums[i]
    num_index[nums[i]], num_index[nums[j]] = num_index[nums[j]], num_index[nums[i]]
    count += 1

print(count)
