import os

with open(f'{os.getcwd()}/2023/Python/day07/input.txt', 'r') as f:
    data = f.read().splitlines()

data = [line.split(' ') for line in data]

print(data)


def assign_type(hand):
    map = {}
    for char in hand:
        if char not in map.keys():
            map[char] = 1
        else:
            map[char] += 1

    print(hand)
    print(map)
    print(f'length:{len(map)}')

    if len(map) == 1:
        return 6  # five of a kind
    elif len(map) == 2 and 4 in map.values():
        return 5  # four of a kind
    elif len(map) == 2 and 3 in map.values() and 2 in map.values():
        return 4  # full house
    elif len(map) == 3 and 3 in map.values():
        return 3  # three of a kind
    elif len(map) == 3 and 1 in map.values() and 2 in map.values():
        return 2  # two pair
    elif len(map) == 4 and 2 in map.values() and 1 in map.values():
        return 1  # one pair
    else:
        return 0  # high card


order = '23456789TJQKA'


def compare_hands(hand1, hand2):
    type1 = assign_type(hand1)
    type2 = assign_type(hand2)

    # print(hand1[0], hand2[0])
    # print(type1, type2)

    if type1 > type2:
        print(f"winning hand: {hand1} with type {type1}")
        return hand1
    elif type1 < type2:
        print(f"winning hand: {hand2} with type {type2}")
        return hand2
    else:  # compare the cards one char at a time
        print('TRIGGERED')
        print(f"{hand1} TYPE: {type1}")
        print(f"{hand2} TYPE: {type2}")
        print('--------------')
        for idx, char in enumerate(hand1):
            print(order.index(char), order.index(hand2[idx]))
            if order.index(char) > order.index(hand2[idx]):
                print(f"winning hand: {hand1} with type {type1}")
                return hand1
            elif order.index(char) < order.index(hand2[idx]):
                print(f"winning hand: {hand2} with type {type2}")
                return hand2
        print('NO WINNER SENT')


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):

            if compare_hands(arr[j][0], arr[j + 1][0]) == arr[j][0]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


bubble_sort(data)

print()
print(data)

ans = 0
for idx, hand in enumerate(data):
    rank = idx + 1
    ans += (int(hand[1]) * rank)

print(ans)
