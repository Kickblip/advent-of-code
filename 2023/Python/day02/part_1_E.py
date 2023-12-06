import os

with open(f'{os.getcwd()}/2023/Python/day02/input.txt', 'r') as f:
    games = {
        game.split(' ')[1]: {
            f"{set_index}-{cube_index}": {'color': color, 'count': count}
            for set_index, set in enumerate(sets.split('; '))
            for cube_index, cube in enumerate(set.split(', '))
            for count, color in [cube.split(' ')]
        }
        for game, sets in (line.split(': ') for line in f.read().splitlines())
    }

print(sum(
    int(game_id) for game_id, game in games.items() if all(
        not ((cube['color'] == 'red' and int(cube['count']) > 12) or
             (cube['color'] == 'green' and int(cube['count']) > 13) or
             (cube['color'] == 'blue' and int(cube['count']) > 14))
        for cube in game.values()
    )
))
