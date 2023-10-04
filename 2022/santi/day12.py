from typing import Tuple
from data_loader import DataLoader


def load_data() -> Tuple[Tuple[Tuple[int]], Tuple[int], Tuple[int]]:
    data_loader = DataLoader(day=12)
    raw_data = data_loader.load().splitlines()

    parsed_data = []
    start_coords = (0, 0)
    end_coords = (0, 0)

    for line_i, line in enumerate(raw_data):
        temp_line = []
        for char_i, char in enumerate(line):
            match char:
                case "S":
                    start_coords = (char_i, line_i)
                    char = "a"
                case "E":
                    end_coords = (char_i, line_i)
                    char = "z"
            temp_line.append(ord(char) - 96)

        parsed_data.append(tuple(temp_line))

    return tuple(parsed_data), start_coords, end_coords


data, start_coords, end_cords = load_data()


def bfs(data: Tuple[Tuple[int]]) -> int:
    pass


def part1():
    pass


if __name__ == "__main__":
    print(part1())
