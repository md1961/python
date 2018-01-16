MIN_DEADLINE = (8 - 6) * 60 + 59

t_walk_before, t_train, t_walk_after = list(map(int, input().split()))
n_trains = int(input())
leave_mins = []
for i in range(n_trains):
    hour, min = list(map(int, input().split()))
    leave_mins.append((hour - 6) * 60 + min)

min_to_arrive = MIN_DEADLINE - t_walk_after
min_to_leave = min_to_arrive - t_train
min_to_catch = max(filter(lambda m: m <= min_to_leave, leave_mins))
min_to_leave_home = min_to_catch - t_walk_before

hour = int(min_to_leave_home / 60)
min = min_to_leave_home - hour * 60
print('{:02}:{:02}'.format(hour + 6, min))
