from data_loader import DataLoader
import heapq

data_loader = DataLoader(1)

data = [cals.split("\n") for cals in data_loader.load().split("\n\n")[:-1]]
for l, _ in enumerate(data): data[l] = sum([int(i) for i in data[l]])

""" PART 1 """
def part1():
    most_calories = 0
    for elf in data:
        if elf > most_calories: most_calories = elf
    print(most_calories)

""" PART 2 """
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
    print(sum(top_calories))

""" PART 2 (Optimized) """
def part2optimized():
    top_calories = []
    for elf in data:
        heapq.heappush(top_calories, elf)
    print(sum(heapq.nlargest(3, top_calories)))

if __name__ == '__main__':
    part1()
    part2()
    part2optimized()