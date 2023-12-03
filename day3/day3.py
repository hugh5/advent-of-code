def part1():
    f = open("day3.input", "r")
    lines = list(map(lambda x: x.strip("\n"), f.readlines()))
    lines = list(map(lambda x: "." + x + ".", lines))

    def check_for_symbol(prev, curr, next, start, end):
        for x in range(max(0, start - 1), min(len(prev), end + 1)):
            if not prev[x].isdigit() and prev[x] != ".":
                return True
            if not curr[x].isdigit() and curr[x] != ".":
                return True
            if not next[x].isdigit() and next[x] != ".":
                return True
        return False

    total = 0
    for y in range(len(lines)):
        previous_line = "." * len(lines[y]) if y == 0 else lines[y - 1]
        line = lines[y]
        next_line = "." * len(lines[y]) if y == len(lines) - 1 else lines[y + 1]

        x = 0
        while x < len(line):
            if line[x].isdigit():
                end = x
                while line[end].isdigit() and end < len(line):
                    end += 1
                number = int(line[x:end])
                if check_for_symbol(previous_line, line, next_line, x, end):
                    total += number

                x = end
                continue
            x += 1
    return total

def part2():
    f = open("day3.input", "r")
    lines = list(map(lambda x: x.strip("\n"), f.readlines()))
    lines = list(map(lambda x: "." + x + ".", lines))

    def find_numbers(line, point):
        nums = []

        x = point - 1
        while x <= point + 1:
            start, end = x, x
            if line[x].isdigit():

                while line[start].isdigit() and start > 0:
                    start -= 1
                while line[end].isdigit() and end < len(line):
                    end += 1
                # print(line[start+1:end])
                nums.append(int(line[start+1:end]))
            x = max(end + 1, x + 1)

        return nums

    total = 0
    for y in range(len(lines)):
        previous_line = "." * len(lines[y]) if y == 0 else lines[y - 1]
        line = lines[y]
        next_line = "." * len(lines[y]) if y == len(lines) - 1 else lines[y + 1]

        x = 0
        while x < len(line):
            if line[x] == "*":
                nums = find_numbers(previous_line, x) + find_numbers(line, x) + find_numbers(next_line, x)
                if len(nums) == 2:
                    total += nums[0] * nums[1]

            x += 1
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
