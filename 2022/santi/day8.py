from typing import Tuple
from data_loader import DataLoader

data_loader = DataLoader(day=8)
raw_data = data_loader.load()

data = raw_data.splitlines()


def visible_left(x, tree, line) -> Tuple[bool, int]:
    for i in range(x - 1, -1, -1):
        if int(tree) <= int(line[i]):
            return False, x - i
    return True, x


def visible_right(x, tree, line) -> Tuple[bool, int]:
    for i in range(x + 1, len(line)):
        if int(tree) <= int(line[i]):
            return False, i - x
    return True, len(range(x, len(line))) - 1


def visible_top(x, y, tree) -> Tuple[bool, int]:
    for i in range(y - 1, -1, -1):
        if int(tree) <= int(data[i][x]):
            return False, y - i
    return True, y


def visible_bottom(x, y, tree) -> Tuple[bool, int]:
    for i in range(y + 1, len(data)):
        if int(tree) <= int(data[i][x]):
            return False, i - (y + 1)
    return True, len(range(y, len(data))) - 1


def part1():
    # count all trees on the borders as visible to begin with
    result = len(data) * 2 + (len(data[0]) - 2) * 2
    for y, line in enumerate(data[1:-1]):
        for x, tree in enumerate(line[1:-1]):
            if int(tree) != 0 and (
                visible_left(x + 1, tree, line)[0]
                or visible_right(x + 1, tree, line)[0]
                or visible_top(x + 1, y + 1, tree)[0]
                or visible_bottom(x + 1, y + 1, tree)[0]
            ):
                result += 1

    return result


def part2():
    max_result = 0
    for y, line in enumerate(data):
        for x, tree in enumerate(line):
            if int(tree) != 0:
                view_dist_mult = (
                    visible_top(x, y, tree)[1]
                    * visible_left(x, tree, line)[1]
                    * visible_bottom(x, y, tree)[1]
                    * visible_right(x, tree, line)[1]
                )
                if view_dist_mult > max_result:
                    max_result = view_dist_mult
    return max_result


if __name__ == "__main__":
    print(part1())
    print(part2())
