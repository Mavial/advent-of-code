from typing import List, Tuple, MutableSet
from data_loader import DataLoader

data_loader = DataLoader(day=9)
raw_data = data_loader.load()
# raw_data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""
data = tuple(
    tuple(
        result if idx != 1 else int(result) for idx, result in enumerate(r.split(" "))
    )
    for r in raw_data.splitlines()
)


def move_head(coords: List[int], n: int, direction: str) -> Tuple[int]:
    match direction:
        case "U":
            return coords[0], coords[1] + n
        case "D":
            return coords[0], coords[1] - n
        case "L":
            return coords[0] - n, coords[1]
        case "R":
            return coords[0] + n, coords[1]


def tail_follows(
    head: List[int], tail: List[int]
) -> Tuple[List[int], MutableSet[Tuple[int]]]:
    abs_distance_x = abs(head[0] - tail[0])
    abs_distance_y = abs(head[1] - tail[1])

    # make sure that head and tail are not overlapping to prevent ZeroDivisionError
    if abs_distance_x == 0 and abs_distance_y == 0:
        return tail, ()

    elif abs_distance_x != 0 and abs_distance_y != 0:
        return tail_follows_diagonal(head, tail, abs_distance_x, abs_distance_y)
    elif abs_distance_y == 0:
        return tail_follows_horiz(head, tail, abs_distance_x, abs_distance_y)
    elif abs_distance_x == 0:
        return tail_follows_vert(head, tail, abs_distance_x, abs_distance_y)
    else:
        exit("Wrong lateral step.")


def tail_follows_diagonal(
    head: Tuple[int], tail: Tuple[int], abs_distance_x: int, abs_distance_y: int
) -> Tuple[Tuple[int], MutableSet[Tuple[int]]]:
    if abs_distance_y == 1:
        return tail_follows_horiz(head, tail, abs_distance_x, abs_distance_y)
    elif abs_distance_x == 1:
        return tail_follows_vert(head, tail, abs_distance_x, abs_distance_y)
    else:
        exit("Wrong diagonal move.")


def tail_follows_horiz(
    head: Tuple[int], tail: Tuple[int], abs_distance_x: int, abs_distance_y: int
):
    tail_trail = set()
    distance_x = abs_distance_x * ((head[0] - tail[0]) // abs(head[0] - tail[0]))
    distance_y = (
        abs_distance_y * ((head[1] - tail[1]) // abs(head[1] - tail[1]))
        if abs_distance_y
        else 0
    )
    for i in range(
        tail[0],
        head[0],
        distance_x // abs(distance_x),
    )[abs_distance_y:]:
        tail_trail.add((i, tail[1] + distance_y))
    new_tail = (
        tail[0] + (distance_x // abs(distance_x)) * (abs(distance_x) - 1),
        tail[1] + distance_y,
    )
    return new_tail, tail_trail


def tail_follows_vert(
    head: Tuple[int], tail: Tuple[int], abs_distance_x: int, abs_distance_y: int
):
    tail_trail = set()
    distance_x = (
        abs_distance_x * ((head[0] - tail[0]) // abs(head[0] - tail[0]))
        if abs_distance_x
        else 0
    )
    distance_y = abs_distance_y * ((head[1] - tail[1]) // abs(head[1] - tail[1]))
    for i in range(
        tail[1],
        head[1],
        distance_y // abs(distance_y),
    )[abs_distance_x:]:
        tail_trail.add((tail[0] + distance_x, i))
    new_tail = (
        tail[0] + distance_x,
        tail[1] + (distance_y // abs(distance_y)) * (abs(distance_y) - 1),
    )
    return new_tail, tail_trail


def tail_too_far(head: List[int], tail: List[int]) -> bool:
    distance_x = abs(abs(head[0] - tail[0]))
    distance_y = abs(abs(head[1] - tail[1]))
    if distance_x > 1 or distance_y > 1:
        return True
    else:
        return False


""" PART 1 """


def part1():
    result = set([(0, 0)])
    #       x, y
    head = (0, 0)
    tail = (0, 0)
    for move in data:
        head = move_head(head, move[1], move[0])
        if tail_too_far(head, tail):
            tail, tail_moves = tail_follows(head, tail)
            result.update(tail_moves)
    return len(result)


if __name__ == "__main__":
    p1 = part1()
    print(len(p1))
