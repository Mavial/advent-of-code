from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=4)
    raw_data = data_loader.load()
    return [
        [[int(i) for i in x.split("-")] for x in r.split(",")]
        for r in raw_data.splitlines()
    ]


data = load_data()


def part1():
    result = 0
    for line in data:
        if (
            line[0][0] <= line[1][0]
            and line[0][1] >= line[1][1]
            or line[0][0] >= line[1][0]
            and line[0][1] <= line[1][1]
        ):
            result += 1
    return result


def part2():
    result = 0
    for line in data:
        if (
            line[0][0] in range(line[1][0], line[1][1] + 1)
            or line[0][1] in range(line[1][0], line[1][1] + 1)
            or line[1][0] in range(line[0][0], line[0][1] + 1)
            or line[1][1] in range(line[0][0], line[0][1] + 1)
        ):
            result += 1
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
