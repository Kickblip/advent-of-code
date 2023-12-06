import os
from functools import reduce

with open(f'{os.getcwd()}/2023/Python/day06/input.txt', 'r') as f:
    data = f.read().splitlines()

s1 = data[0].split(':')
times = [time for time in s1[1].split(" ") if time]
time = ''.join(times)

s2 = data[1].split(':')
distances = [time for time in s2[1].split(" ") if time]
distance = ''.join(distances)

possible_distances = []

for x in range(1, int(time) + 1):
    time_travelling = int(time) - x
    length = x * time_travelling
    if length > int(distance):
        possible_distances.append(distance)

print(reduce((lambda x, y: x * y), [len(possible_distances)]))
