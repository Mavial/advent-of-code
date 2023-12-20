from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=5, year=2023)
    raw_data = data_loader.load()

    split_maps = raw_data.split("\n\n")
    seeds = split_maps[0].split(": ")[1].split(" ")
    parsed_maps = [
        [vals.split() for vals in map_data.splitlines()[1:]]
        for map_data in split_maps[1:]
    ]
    return tuple(map(lambda x: int(x), seeds)), parsed_maps


seeds, maps = load_data()


def parse_map(maps=maps) -> list[list[tuple[int, int, int]]]:
    map_list = []
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
    return map_list


map_list = parse_map()


def part1(seeds=seeds):  # NOSONAR
    result = float("inf")
    for seed in seeds:
        for m in map_list:
            for row in m:
                if seed >= row[0] and seed <= row[1]:
                    seed = seed + row[2]
                    break
        result = seed if seed < result else result
    return result


def split_ranges(seed_range, row) -> tuple[tuple, tuple]:
    if seed_range[0] <= row[0] and seed_range[1] >= row[1]:  # seed range contains row
        if seed_range[0] == row[0]:
            return (
                (
                    tuple(
                        (
                            row[0] + row[2],
                            row[1] + row[2],
                        )
                    ),
                ),
                (
                    tuple(
                        (
                            row[1] + 1,
                            seed_range[1],
                        )
                    ),
                ),
            )
        elif seed_range[1] == row[1]:
            return (
                (
                    tuple(
                        (
                            row[0] + row[2],
                            row[1] + row[2],
                        )
                    ),
                ),
                (
                    tuple(
                        (
                            seed_range[0],
                            row[0] - 1,
                        )
                    ),
                ),
            )
        else:
            return (
                (
                    tuple(
                        (
                            row[0] + row[2],
                            row[1] + row[2],
                        )
                    ),
                ),
                (
                    tuple(
                        (
                            seed_range[0],
                            row[0] - 1,
                        )
                    ),
                    tuple(
                        (
                            row[1] + 1,
                            seed_range[1],
                        )
                    ),
                ),
            )
    elif seed_range[0] <= row[1] and seed_range[1] > row[1]:  # seed range starts in row
        return (
            (
                tuple(
                    (
                        seed_range[0] + row[2],
                        row[1] + row[2],
                    )
                ),
            ),
            (
                tuple(
                    (
                        row[1] + 1,
                        seed_range[1],
                    )
                ),
            ),
        )
    elif seed_range[0] < row[0] and seed_range[1] >= row[0]:  # seed range ends in row
        return (
            (
                tuple(
                    (
                        row[0] + row[2],
                        seed_range[1] + row[2],
                    ),
                ),
            ),
            (
                tuple(
                    (
                        seed_range[0],
                        row[0] - 1,
                    )
                ),
            ),
        )
    elif (
        seed_range[0] >= row[0] and seed_range[1] <= row[1]
    ):  # seed range is contained in row
        return (
            (
                tuple(
                    (
                        seed_range[0] + row[2],
                        seed_range[1] + row[2],
                    )
                ),
            ),
            tuple(),
        )
    else:
        return tuple(), tuple((seed_range,))


def part2():
    # Initialize the result with the maximum possible value
    minimum_low_seed = float("inf")

    # Iterate over the seeds in pairs
    for i in range(0, len(seeds), 2):
        # Initialize seed_ranges with the current pair of seeds
        seed_ranges = [(seeds[i], seeds[i] + (seeds[i + 1] - 1))]

        # Process each map in the map_list
        for map in map_list:
            modified_seed_ranges = []

            # Process each row in the current map
            for row in map:
                new_seed_ranges = []

                # Process each seed range
                for seed_range in seed_ranges:
                    # Split the seed range based on the current row
                    modified_seeds, unmodified_seeds = split_ranges(seed_range, row)

                    # Add the unmodified seeds to new seed ranges
                    if unmodified_seeds:
                        new_seed_ranges.extend(unmodified_seeds)

                    # Add the modified seeds to the modified seed ranges
                    modified_seed_ranges.extend(modified_seeds)

                # Update seed_ranges for the next iteration
                seed_ranges = new_seed_ranges

            # Extend seed_ranges with the modified seeds from this map
            seed_ranges.extend(modified_seed_ranges)

        # Find the lowest seed in the current seed ranges
        low_seed = min(start for start, end in seed_ranges)

        # Update the result if a new lower seed is found
        minimum_low_seed = min(minimum_low_seed, low_seed)

    return minimum_low_seed



if __name__ == "__main__":
    print(part1())
    print(part2())
