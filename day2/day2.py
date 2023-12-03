RED = "red"
GREEN = "green"
BLUE = "blue"
max_cubes = (12, 13, 14)


def part1():
    f = open("day2.input", "r")
    total = 0

    while True:
        line = f.readline().strip("\n")
        if not line:
            break

        name, line = line.split(": ")
        id = int(name.split(" ")[1])
        grabs = line.split("; ")
        valid = True
        for grab in grabs:
            sequence = grab.split(", ")
            for event in sequence:
                count, color = event.split(" ")
                if color == RED:
                    if int(count) > max_cubes[0]:
                        valid = False
                        break
                elif color == GREEN:
                    if int(count) > max_cubes[1]:
                        valid = False
                        break
                elif color == BLUE:
                    if int(count) > max_cubes[2]:
                        valid = False
                        break

            if not valid:
                break

        if valid:
            total += id

    return total


def part2():
    f = open("day2.input", "r")
    total = 0

    while True:
        line = f.readline().strip("\n")
        if not line:
            break

        line = line.split(": ")[1]
        game = line.split("; ")
        fewest = [0, 0, 0]
        for grab in game:
            sequence = grab.split(", ")
            for event in sequence:
                count, color = event.split(" ")
                if color == RED:
                    if int(count) > fewest[0]:
                        fewest[0] = int(count)
                elif color == GREEN:
                    if int(count) > fewest[1]:
                        fewest[1] = int(count)
                elif color == BLUE:
                    if int(count) > fewest[2]:
                        fewest[2] = int(count)
        print(fewest)
        total += fewest[0] * fewest[1] * fewest[2]
    return total


if __name__ == "__main__":
    # print(part1())
    print(part2())
