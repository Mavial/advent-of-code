from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=8, year=2023)
    raw_data = data_loader.load()
    #     raw_data = """LR

    # 11A = (11B, XXX)
    # 11B = (XXX, 11Z)
    # 11Z = (11B, XXX)
    # 22A = (22B, XXX)
    # 22B = (22C, 22C)
    # 22C = (22Z, 22Z)
    # 22Z = (22B, 22B)
    # XXX = (XXX, XXX)"""

    directions, raw_nodes = raw_data.split("\n\n")
    nodes = {}

    for line in raw_nodes.splitlines():
        key, data = line.split(" = ")
        nodes[key] = tuple(data[1:-1].split(", "))

    return directions, nodes


DIRECTIONS, NODES = load_data()


def part1():
    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        direction = DIRECTIONS[steps % len(DIRECTIONS)]
        current_node = (
            NODES[current_node][0] if direction == "L" else NODES[current_node][1]
        )
        steps += 1

    return steps


def part2():
    def check_finished(current_nodes) -> bool:
        for node in current_nodes:
            if not node.endswith("Z"):
                return False
        return True

    current_nodes = [n for n in NODES.keys() if n.endswith("A")]
    steps = 0

    while not check_finished(current_nodes):
        direction = DIRECTIONS[steps % len(DIRECTIONS)]
        new_nodes = []
        for node in current_nodes:
            if direction == "L":
                new_nodes.append(NODES[node][0])
            else:
                new_nodes.append(NODES[node][1])
        current_nodes = new_nodes
        steps += 1

    return steps


from collections import deque


# ['AAA', 'RLA', 'QLA', 'QFA', 'RXA', 'JSA']
def find_cycle():
    slow_pointer = "RLA"
    fast_pointer = "RLA"

    slow_tail = deque()
    fast_tail = deque()

    steps = 0

    while True:
        direction = DIRECTIONS[steps % len(DIRECTIONS)]
        if direction == "L":
            fast_pointer = NODES[fast_pointer][0]
            if steps % 2 > 0:
                slow_pointer = NODES[slow_pointer][0]
        else:
            fast_pointer = NODES[fast_pointer][1]
            if steps % 2 > 0:
                slow_pointer = NODES[slow_pointer][1]
        steps += 1

        if len(fast_tail) > 5:
            fast_tail.popleft()
        fast_tail.append(fast_pointer)
        if steps % 2 == 0:
            if len(slow_tail) > 5:
                slow_tail.popleft()
            slow_tail.append(slow_pointer)

        if slow_tail == fast_tail:
            return steps, slow_tail, fast_tail


if __name__ == "__main__":
    # print(part1())
    # print(part2())
    print(find_cycle())
