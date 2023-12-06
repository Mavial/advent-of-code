from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=4, year=2023)
    raw_data = data_loader.load()
    return [
        [
            segment.strip().replace("  ", " ")
            for segment in line.split(": ")[1].split(" | ")
        ]
        for line in raw_data.splitlines()
    ]


data = load_data()


def part1():
    result = 0
    mem = {}  # card no: (win_count, card_amount)
    for i, card in enumerate(data, 1):
        win_count = 0
        winners = tuple(card[0].split(" "))
        numbers = set(card[1].split(" "))

        for winner in winners:
            if winner in numbers:
                win_count += 1
        result += int(2 ** (win_count - 1))
        mem[i] = (win_count, 1)
    return result, mem


def part2(mem: dict[int, tuple[int, int]]):
    for i in range(1, len(mem)):
        for copy in range(i + 1, i + 1 + mem[i][0]):
            mem[copy] = (mem[copy][0], mem[i][1] + mem[copy][1])
    return sum(map(lambda x: x[1], mem.values()))


if __name__ == "__main__":
    result1, mem = part1()
    print(result1)
    print(part2(mem))
