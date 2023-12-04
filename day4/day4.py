import math
from collections import defaultdict

def part1():
    f = open("day4.input", "r")
    total = 0
    while True:
        line = f.readline()
        if not line:
            break

        matches = 0
        line = line.split(": ")[1]
        winning, player = line.split(" | ")
        winning = list(filter(lambda x: x != "", winning.split(" ")))
        player = list(filter(lambda x: x != "", player.split(" ")))
        wset = set(map(lambda x: int(x), winning))
        pset = set(map(lambda x: int(x), player))
        print(wset, pset)
        for w in wset:
            if w in pset:
                matches += 1
        total += math.floor(pow(2, matches-1))
    return total

def part2():
    f = open("day4.input", "r")
    num_cards = defaultdict(lambda: 1)
    num_cards[1] = 1
    total = 0
    card_num = 1
    while True:
        line = f.readline()
        if not line:
            break

        matches = 0
        line = line.split(": ")[1]
        winning, player = line.split(" | ")
        winning = list(filter(lambda x: x != "", winning.split(" ")))
        player = list(filter(lambda x: x != "", player.split(" ")))
        wset = set(map(lambda x: int(x), winning))
        pset = set(map(lambda x: int(x), player))
        print(wset, pset)
        for w in wset:
            if w in pset:
                matches += 1

        for i in range(card_num+1, card_num+matches+1):
            num_cards[i] += num_cards[card_num]
        total += num_cards[card_num]
        card_num += 1

    return total


if __name__ == "__main__":
    # print(part1())
    print(part2())
