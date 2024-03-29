from data_loader import DataLoader
import heapq


def load_data():
    data_loader = DataLoader(day=1)
    data = [cals.split("\n") for cals in data_loader.load().split("\n\n")[:-1]]
    for l, _ in enumerate(data):
        data[l] = sum([int(i) for i in data[l]])
    return data


data = load_data()


def part1():
    most_calories = 0
    for elf in data:
        if elf > most_calories:
            most_calories = elf
    return most_calories


def part2():
    top_calories = data[:3]
    top_calories.sort()
    for elf in data:
        if elf > top_calories[0]:
            if elf > top_calories[1]:
                if elf > top_calories[2]:
                    top_calories[0] = top_calories[1]
                    top_calories[1] = top_calories[2]
                    top_calories[2] = elf
                else:
                    top_calories[0] = top_calories[1]
                    top_calories[1] = elf
            else:
                top_calories[0] = elf
    return sum(top_calories)


""" PART 2 (Optimized) """


def part2optimized():
    top_calories = []
    for elf in data:
        heapq.heappush(top_calories, elf)
    return sum(heapq.nlargest(3, top_calories))


if __name__ == "__main__":
    print(part1())
    print(part2())
    print(part2optimized())
