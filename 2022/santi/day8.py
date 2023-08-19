from typing import Tuple
from collections import deque
from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=8)
    raw_data = data_loader.load()

    data = tuple(int(i) for i in raw_data.replace("\n", ""))
    sorted_data = [deque() for _ in range(10)]
    return data, sorted_data

data, sorted_data = load_data()

# delimiter to skip lower trees since they are less likely to be visible from far away
MIN_TREE_SIZE = 0
ROW_LEN = 99

for i, val in enumerate(data):
    x = i % ROW_LEN
    y = i // ROW_LEN
    sorted_data[val].append((x, y))


def visible_left(x, y, tree) -> Tuple[bool, int]:
    for i in range(x - 1, -1, -1):
        if int(tree) <= int(data[y * ROW_LEN + i]):
            return False, x - i
    return True, x


def visible_right(x, y, tree) -> Tuple[bool, int]:
    for i in range(x + 1, ROW_LEN):
        if int(tree) <= int(data[y * ROW_LEN + i]):
            return False, i - x
    return True, len(range(x, ROW_LEN)) - 1


def visible_top(x, y, tree) -> Tuple[bool, int]:
    for i in range(y - 1, -1, -1):
        if int(tree) <= int(data[i * ROW_LEN + x]):
            return False, y - i
    return True, y


def visible_bottom(x, y, tree) -> Tuple[bool, int]:
    for i in range(y + 1, len(data) // ROW_LEN):
        if int(tree) <= int(data[i * ROW_LEN + x]):
            return False, i - (y + 1)
    return True, len(range(y, len(data) // ROW_LEN)) - 1


def part1():
    # count all trees on the borders as visible to begin with
    result = 0
    for value in range(9, -1, -1):
        for tree in sorted_data[value]:
            if (
                visible_left(tree[0], tree[1], value)[0]
                or visible_right(tree[0], tree[1], value)[0]
                or visible_top(tree[0], tree[1], value)[0]
                or visible_bottom(tree[0], tree[1], value)[0]
            ):
                result += 1
    return result


def part2():
    max_result = 0
    for value in range(9, -1, -1):
        for tree in sorted_data[value]:
            view_dist_mult = (
                visible_left(tree[0], tree[1], value)[1]
                * visible_right(tree[0], tree[1], value)[1]
                * visible_top(tree[0], tree[1], value)[1]
                * visible_bottom(tree[0], tree[1], value)[1]
            )
            if view_dist_mult > max_result:
                max_result = view_dist_mult
    return max_result


if __name__ == "__main__":
    print(part1())
    print(part2())
