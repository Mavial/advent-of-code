from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=3)
    return data_loader.load().split("\n")


data = load_data()


def part1():
    result = 0
    for rucksack in data:
        used_chars = []
        f, b = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]

        for char in f:
            if char in b and char not in used_chars:
                used_chars.append(char)
                if char.islower():
                    result += ord(char) - 96
                else:
                    result += ord(char) - 38

    return result


def part2():
    result = 0
    for rucksack in range(0, len(data), 3):
        used_chars = []
        elf_group = data[rucksack : rucksack + 3]

        for char in elf_group[0]:
            if char in elf_group[1] and char in elf_group[2] and char not in used_chars:
                used_chars.append(char)
                if char.islower():
                    result += ord(char) - 96
                else:
                    result += ord(char) - 38

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
