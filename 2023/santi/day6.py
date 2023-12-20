from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=6, year=2023)
    raw_data = data_loader.load()

    lines = [line.split(":")[1].strip().split() for line in raw_data.split("\n")]
    races = [(time, lines[1][i]) for i, time in enumerate(lines[0])]
    return races


races = load_data()

def part1():
    result = 1
    for race in races:
        ways_to_win = 0
        total_racetime, distance_to_beat = map(int, race)
        for time_held in range(1, total_racetime):
            if (total_racetime - time_held) * time_held > distance_to_beat:
                ways_to_win += 1
        result *= ways_to_win
    return result

def part2():
    race = (int(''.join(x)) for x in zip(*races))
    ways_to_win = 0
    total_racetime, distance_to_beat = map(int, race)
    for time_held in range(1, total_racetime):
        if (total_racetime - time_held) * time_held > distance_to_beat:
            ways_to_win += 1
    return ways_to_win

if __name__ == "__main__":
    print(part1())
    print(part2())