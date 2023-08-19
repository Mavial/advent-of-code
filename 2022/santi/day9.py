from typing import List, Tuple, MutableSet, Generator
from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=9)
    raw_data = data_loader.load()

    return tuple(
        tuple(
            result if idx != 1 else int(result)
            for idx, result in enumerate(r.split(" "))
        )
        for r in raw_data.splitlines()
    )


data = load_data()


def move_head(
    coords: List[int], n: int, direction: str, step_by_step: bool = False
) -> Generator[Tuple[int], None, None]:
    """Move a head in the specified direction by n steps."""

    deltas = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    dx, dy = deltas[direction]

    if step_by_step:
        for _ in range(n):
            coords = coords[0] + dx, coords[1] + dy
            yield coords
    else:
        yield coords[0] + dx * n, coords[1] + dy * n


def tail_follows(
    head: List[int], tail: List[int]
) -> Tuple[List[int], MutableSet[Tuple[int]]]:
    """Compute the movement of the tail based on the head's position."""

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
    """Handle the tail's diagonal movement."""

    if abs_distance_x == abs_distance_y and abs_distance_x == 2 or abs_distance_y == 1:
        return tail_follows_horiz(
            head, tail, abs_distance_x, abs_distance_y, is_diag=True
        )
    elif abs_distance_x == 1:
        return tail_follows_vert(
            head, tail, abs_distance_x, abs_distance_y, is_diag=True
        )
    else:
        exit("Wrong diagonal move.")


def tail_follows_horiz(
    head: Tuple[int],
    tail: Tuple[int],
    abs_distance_x: int,
    abs_distance_y: int,
    is_diag: bool = False,
):
    """Handle the tail's horizontal movement."""

    tail_trail = set()
    distance_x = abs_distance_x * ((head[0] - tail[0]) // abs(head[0] - tail[0]))
    distance_y = (
        abs_distance_y * ((head[1] - tail[1]) // abs(head[1] - tail[1]))
        if abs_distance_y
        else 0
    )
    diag_offset = distance_y // abs(distance_y) if is_diag else 0

    for i in range(
        tail[0],
        head[0],
        distance_x // abs(distance_x),
    )[abs(diag_offset) :]:
        tail_trail.add((i, tail[1] + diag_offset))
    new_tail = (
        tail[0] + (distance_x // abs(distance_x)) * (abs(distance_x) - 1),
        tail[1] + diag_offset,
    )
    return new_tail, tail_trail


def tail_follows_vert(
    head: Tuple[int],
    tail: Tuple[int],
    abs_distance_x: int,
    abs_distance_y: int,
    is_diag: bool = False,
):
    """Handle the tail's vertical movement."""

    tail_trail = set()
    distance_x = (
        abs_distance_x * ((head[0] - tail[0]) // abs(head[0] - tail[0]))
        if abs_distance_x
        else 0
    )
    distance_y = abs_distance_y * ((head[1] - tail[1]) // abs(head[1] - tail[1]))
    diag_offset = distance_x // abs(distance_x) if is_diag else 0

    for i in range(
        tail[1],
        head[1],
        distance_y // abs(distance_y),
    )[abs(diag_offset) :]:
        tail_trail.add((tail[0] + diag_offset, i))
    new_tail = (
        tail[0] + diag_offset,
        tail[1] + (distance_y // abs(distance_y)) * (abs(distance_y) - 1),
    )
    return new_tail, tail_trail


def tail_too_far(head: Tuple[int], tail: Tuple[int]) -> bool:
    """Determine if the distance between the head and tail is too large."""

    distance_x = abs(abs(head[0] - tail[0]))
    distance_y = abs(abs(head[1] - tail[1]))
    if distance_x > 1 or distance_y > 1:
        return True
    else:
        return False


def part1():
    result = {(0, 0)}
    #       x, y
    head = (0, 0)
    tail = (0, 0)
    for move in data:
        head = next(move_head(head, move[1], move[0]))
        if tail_too_far(head, tail):
            tail, tail_moves = tail_follows(head, tail)
            result.update(tail_moves)
    return len(result)


def part2():
    result = {(0, 0)}
    knots = [(0, 0)] * 10

    for direction, distance in data:
        for head_pos in move_head(knots[0], distance, direction, step_by_step=True):
            knots[0] = head_pos
            update_knots_and_result(knots, result)

    return len(result)


def update_knots_and_result(
    knots: List[Tuple[int, int]], result: MutableSet[Tuple[int, int]]
):
    for i, knot in enumerate(knots[1:], 1):
        prev_knot = knots[i - 1]
        if tail_too_far(prev_knot, knot):
            new_knot, tail_moves = tail_follows(prev_knot, knot)
            knots[i] = new_knot
            if i == 9:
                result.update(tail_moves)
        else:
            break


if __name__ == "__main__":
    print(part1())
    print(part2())
