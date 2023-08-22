from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=10)
    raw_data = data_loader.load()

    return tuple(tuple(line.split(" ")) for line in raw_data.splitlines())


data = load_data()


def part1():
    x = 1
    cycle = 0
    result = 0
    for instruction in data:
        for _ in instruction:
            cycle += 1
            if cycle == 20 or (cycle - 20) % 40 == 0:
                print(f"{cycle} * {x} = {x*cycle}")
                result += x * cycle
        if len(instruction) == 2:
            x += int(instruction[1])

    return result


def part2():
    x = 1
    cycle = 0
    row = []
    result = []
    for instruction in data:
        for _ in instruction:
            if (
                cycle % 40 - 1 == x % 40
                or cycle % 40 == x % 40
                or cycle % 40 + 1 == x % 40
            ):
                row.append("#")
            else:
                row.append(".")
            cycle += 1
            if len(row) == 40:
                result.append("".join(row))
                row = []
        if len(instruction) == 2:
            x += int(instruction[1])
    return "\n".join(result)


if __name__ == "__main__":
    print(part1())
    print(part2())
