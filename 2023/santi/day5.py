from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=5, year=2023)
    raw_data = data_loader.load()
    #     raw_data = """seeds: 79 14 55 13

    # seed-to-soil map:
    # 50 98 2
    # 52 50 48

    # soil-to-fertilizer map:
    # 0 15 37
    # 37 52 2
    # 39 0 15

    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4

    # water-to-light map:
    # 88 18 7
    # 18 25 70

    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13

    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69

    # humidity-to-location map:
    # 60 56 37
    # 56 93 4"""
    split_maps = raw_data.split("\n\n")
    seeds = split_maps[0].split(": ")[1].split(" ")
    parsed_maps = [
        [vals.split() for vals in map_data.splitlines()[1:]]
        for map_data in split_maps[1:]
    ]
    return tuple(map(lambda x: int(x), seeds)), parsed_maps


seeds, maps = load_data()


def part1(seeds=seeds):  # NOSONAR
    result = 10**40
    map_list: list[list[tuple[int, int, int]]] = []
    for m in maps:
        row_list = []
        for row in m:
            destination_range_start, source_range_start, range_length = map(
                lambda x: int(x), row
            )
            source_range_end = source_range_start + (range_length - 1)
            source_to_destination_offset = destination_range_start - source_range_start
            row_list.append(
                (source_range_start, source_range_end, source_to_destination_offset)
            )
        map_list.append(row_list)
    for seed in seeds:
        for m in map_list:
            for row in m:
                if seed >= row[0] and seed <= row[1]:
                    seed = seed + row[2]
                    break
        result = seed if seed < result else result
    return result


def part2():
    result = 10**40
    for i in range(0, len(seeds), 2):
        print(str((i / len(seeds)) * 100) + "%")
        r = part1(range(seeds[i], seeds[i] + (seeds[i + 1] - 1)))
        if r < result:
            result = r
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
