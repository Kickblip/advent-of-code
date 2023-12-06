import os
from functools import reduce

with open(f'{os.getcwd()}/2023/Python/day06/input.txt', 'r') as f:
    data = f.read().splitlines()

s1 = data[0].split(':')
times = [time for time in s1[1].split(" ") if time]

s2 = data[1].split(':')
distances = [time for time in s2[1].split(" ") if time]

ans = []

for idx, time in enumerate(times):
    possible_distances = []
    for x in range(1, int(time) + 1):
        time_travelling = int(time) - x
        distance = x * time_travelling
        possible_distances.append(distance)

    possible_distances = [
        distance for distance in possible_distances if distance > int(distances[idx])]
    ans.append(len(possible_distances))

print(reduce((lambda x, y: x * y), ans))
