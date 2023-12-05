from data_loader import DataLoader
from functools import reduce


def load_data():
    data_loader = DataLoader(day=2, year=2023)
    raw_data = data_loader.load()
    data = []
    for line in raw_data.splitlines():
        data.append(
            [subset.split(", ") for subset in line.split(":")[1].strip().split("; ")]
        )
    return data


data = load_data()


def part1():
    result = 0
    for i, game in enumerate(data, 1):
        passed = 0
        for subset in game:
            cubes = {"red": 0, "green": 0, "blue": 0}
            for cube in subset:
                count, color = cube.split(" ")
                cubes[color] += int(count)
            if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
                passed += 1
        if passed == len(game):
            result += i
    return result


def part2():
    result = 0
    for game in data:
        cubes = {"red": 0, "green": 0, "blue": 0}
        for subset in game:
            for cube in subset:
                count, color = cube.split(" ")
                count = int(count)
                if count > cubes[color]:
                    cubes[color] = count
        result += reduce((lambda x, y: x * y), cubes.values())
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
