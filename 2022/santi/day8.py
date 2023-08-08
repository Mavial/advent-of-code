from collections import deque
from data_loader import DataLoader

data_loader = DataLoader(day=8)
raw_data = data_loader.load()

data = raw_data.splitlines()
data = """30373
25512
65332
33549
35390""".splitlines()

""" PART 1 """


def visible_left(x, tree, line) -> bool:
    for i in range(x + 1):
        if int(tree) <= int(line[i]):
            return False
    return True


def visible_right(x, tree, line) -> bool:
    for i in range(x + 2, len(line)):
        if int(tree) <= int(line[i]):
            return False
    return True


def visible_top(x, y, tree) -> bool:
    for i in range(y + 1):
        if int(tree) <= int(data[i][x + 1]):
            return False
    return True


def visible_bottom(x, y, tree) -> bool:
    for i in range(y + 2, len(data)):
        if int(tree) <= int(data[i][x + 1]):
            return False
    return True


def part1():
    # count all trees on the borders as visible to begin with
    result = len(data) * 2 + (len(data[0]) - 2) * 2
    for y, line in enumerate(data[1:-1]):
        for x, tree in enumerate(line[1:-1]):
            if int(tree) != 0 and (
                visible_left(x, tree, line)
                or visible_right(x, tree, line)
                or visible_top(x, y, tree)
                or visible_bottom(x, y, tree)
            ):
                result += 1

    return result

def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
