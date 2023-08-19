from collections import deque
from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=5)
    raw_data = data_loader.load()

    """ Prepare the data by separating stacks from moves and serializing stacks and moves to machine readable arrays."""
    raw_stacks, raw_moves = raw_data.split("\n\n")

    num_stacks = int(raw_stacks[-2:])
    stacks = [deque() for _ in range(num_stacks)]
    stacks_list = [
        list() for _ in range(num_stacks)
    ]  # Part 2 requires an array instead of a stack

    for line in raw_stacks[::-1].splitlines()[1:]:
        line = line.replace("[", " ").replace("]", " ")
        line = "".join([line[i] for i in range(1, len(line), 4)])
        for i, crate in enumerate(line[::-1]):
            if crate != " ":
                stacks[i].append(crate)
            if crate != " ":
                stacks_list[i].append(crate)

    moves = [
        [
            int(i)
            for i in move.replace("move ", "")
            .replace("from ", "")
            .replace("to ", "")
            .split(" ")
        ]
        for move in raw_moves.splitlines()
    ]
    return moves, stacks, stacks_list


moves, stacks, stacks_list = load_data()

""" PART 1 """


def part1():
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

    result = []
    for stack in stacks:
        result.append(stack[-1])
    return "".join(result)


""" PART 2 """


def part2():
    for move in moves:
        stacks_list[move[2] - 1] = (
            stacks_list[move[2] - 1] + stacks_list[move[1] - 1][-move[0] :]
        )
        stacks_list[move[1] - 1] = stacks_list[move[1] - 1][: -move[0]]

    result = []
    for l in stacks_list:
        result.append(l[-1])
    return "".join(result)


if __name__ == "__main__":
    print(part1())
    print(part2())
