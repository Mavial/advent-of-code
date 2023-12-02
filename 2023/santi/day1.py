from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=1, year=2023)
    raw_data = data_loader.load()
    return raw_data.splitlines()


data = load_data()


def part1():
    result = []
    for line in data:
        for i, c in enumerate(line):
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                dig_first = c
                break
        for i, c in enumerate(line[::-1]):
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                i = len(line) - i - 1
                dig_last = c
                break
        result.append(int(dig_first + dig_last))
    return sum(result)


def find_and_index_spelt_digits(line: str, min_max_index: list[tuple[int, str]]):
    spelt = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for digstr in spelt.keys():
        min_i = line.find(digstr)
        max_i = -1

        reverse_index = line[::-1].find(digstr[::-1])
        if reverse_index > -1:
            max_i = len(line) - len(digstr) - reverse_index

        if min_i != -1 and min_i < min_max_index[0][0]:
            min_max_index[0] = (min_i, spelt[digstr])
        if max_i != -1 and max_i > min_max_index[1][0]:
            min_max_index[1] = (max_i, spelt[digstr])
    return int(min_max_index[0][1] + min_max_index[1][1])


def get_min_max_index(ind, dig_first, dig_last):
    return [
        (min(ind) if ind else 99, dig_first),
        (max(ind) if ind else 0, dig_last),
    ]


def part2():
    result = []
    for line in data:
        ind = []
        # find digits
        for i, c in enumerate(line):
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                ind.append(i)
                dig_first = c
                break
        for i, c in enumerate(line[::-1]):
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                i = len(line) - i - 1
                ind.append(i)
                dig_last = c
                break
        min_max_index = get_min_max_index(ind, dig_first, dig_last)  # index, val

        # find spelt digits
        result.append(find_and_index_spelt_digits(line, min_max_index))

    return sum(result)


if __name__ == "__main__":
    print(part1())
    print(part2())
