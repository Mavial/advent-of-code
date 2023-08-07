from collections import deque
from data_loader import DataLoader

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

move_cleaner = lambda move: [
    int(i)
    for i in move.replace("move ", "")
    .replace("from ", "")
    .replace("to ", "")
    .split(" ")
]
moves = [move_cleaner(move) for move in raw_moves.splitlines()]

""" PART 1 """
for move in moves:
    for _ in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

for stack in stacks:
    print(stack[-1], end="")
print("")


""" PART 2 """
for move in moves:
    stacks_list[move[2] - 1] = (
        stacks_list[move[2] - 1] + stacks_list[move[1] - 1][-move[0] :]
    )
    stacks_list[move[1] - 1] = stacks_list[move[1] - 1][: -move[0]]

for list in stacks_list:
    print(list[-1], end="")
print("")
