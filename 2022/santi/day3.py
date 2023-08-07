from data_loader import DataLoader

data_loader = DataLoader(day=3)

data = data_loader.load().split("\n")

""" PART 1 """
def part1():
    result = 0
    for rucksack in data:
        used_chars = []
        f, b = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]

        for char in f:
            if char in b and char not in used_chars:
                used_chars.append(char)
                if char.islower():
                    result += ord(char) - 96
                else:
                    result += ord(char) - 38

    print(result)

""" PART 2 """
def part2():
    result = 0
    for rucksack in range(0, len(data), 3):
        used_chars = []
        elf_group = data[rucksack:rucksack + 3]

        for char in elf_group[0]:
            if char in elf_group[1] and char in elf_group[2] and char not in used_chars:
                used_chars.append(char)
                if char.islower():
                    result += ord(char) - 96
                else:
                    result += ord(char) - 38

    print(result)


if __name__ == '__main__':
    part1()
    part2()