from typing import List, Set
import os


# Represents one specific map
class Interval:
    def __init__(self, start=0, length=0, offset=0, line=''):
        if len(line) > 0:
            dest, start, length = [int(x) for x in line.split(' ')]
            offset = dest - start
        self.start = start
        self.end = start + length - 1
        self.offset = offset

    def contains(self, point: int):
        return self.start <= point <= self.end

    def map(self, point: int):
        return point + self.offset

    def outputs(self, mapped_point: int):
        return self.start + self.offset <= mapped_point <= self.end + self.offset

    def undo_map(self, mapped_point: int):
        return mapped_point - self.offset


class IntervalList:
    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals

    def process(self, point: int):
        for interval in self.intervals:
            if interval.contains(point):
                return interval.map(point)
        return point

    def undo_process(self, outputs: Set[int]):
        potential_inputs = set()
        for interval in self.intervals:
            for output in outputs:
                if interval.outputs(output):
                    potential_inputs.add(interval.undo_map(output))
        outputs.update(potential_inputs)

    def filter(self, points: Set[int]):
        results = set()
        for point in points:
            if any(interval.contains(point) for interval in self.intervals):
                results.add(point)
        return results

    def boundaries(self, candidate_points: Set[int]):
        for interval in self.intervals:
            candidate_points.add(interval.start)
            candidate_points.add(interval.end)


def parse_input(input):
    input += '\n'
    lines = iter(input.split('\n'))

    # Parse the line of seeds
    seed_input, _ = next(lines).split(': ')[1], next(lines)
    seeds = [int(seed) for seed in seed_input.split(' ')]
    seed_intervals = [Interval(seeds[i], seeds[i+1])
                      for i in range(0, len(seeds), 2)]
    seed_intervals = IntervalList(seed_intervals)

    # Will contain the seven layers of maps
    interval_lists: List[IntervalList] = []

    for x in range(7):
        # Skip the blank line and header lines
        _, line = next(lines), next(lines)

        intervals = []
        while len(line) != 0:
            intervals.append(Interval(line=line))
            line = next(lines)

        interval_list = IntervalList(intervals)  # One layer of maps
        interval_lists.append(interval_list)

    return seeds, seed_intervals, interval_lists


def part1(seeds: List[int], interval_lists: List[IntervalList]):
    min_seed = float('inf')
    for seed in seeds:
        # Process the seed in each of the seven layers
        for intervalList in interval_lists:
            seed = intervalList.process(seed)
        min_seed = seed if seed < min_seed else min_seed
    return min_seed


def part2(seed_intervals: IntervalList, interval_lists: List[IntervalList]):

    # Set of input seeds which can potentially results in the optimal location
    candidate_points = set()
    # Go in reverse order from the last map to the first map
    for intervalList in interval_lists[::-1]:
        # Undo the processing for candidate_points from lower maps
        intervalList.undo_process(candidate_points)
        # This map layer contributes its boundaries as candidates
        intervalList.boundaries(candidate_points)

    # Remove candidates that are not valid
    candidate_points = seed_intervals.filter(candidate_points)

    # Test the candidates and find the optimal one
    return part1(candidate_points, interval_lists)


def solution(input):
    seeds, seed_intervals, interval_lists = parse_input(input)

    part1_ans = part1(seeds, interval_lists)
    print(f'Part 1 Answer: {part1_ans}')

    part2_ans = part2(seed_intervals, interval_lists)
    print(f'Part 2 Answer: {part2_ans}')


with open(f'{os.getcwd()}/day05/input.txt', 'r') as f:
    data = f.read()

solution(data)
