from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=3, year=2023)
    raw_data = data_loader.load()
    return raw_data.splitlines()


data = load_data()


class FullNum:
    def __init__(self, x: int, y: int):
        self.start_x, self.end_x, self.val, self.skip_by = self.get_full_num(x, y)
        self.y = y

    def get_full_num(self, x, y) -> (int, int): # NOSONAR
        """Returns the start_x, end_x, and the full number found at data[y][x]."""
        full_num = ""

        def extract_number(start, forward=True):
            num = ""
            still_digit = True
            while still_digit:
                curr_char = data[y][start]
                if curr_char.isdigit():
                    num = num + curr_char if forward else curr_char + num
                    start = start + 1 if forward else start - 1
                    if (forward and start >= len(data[y])) or (
                        not forward and start < 0
                    ):
                        break
                else:  # not a number
                    still_digit = False
            return start - 1 if forward else start + 1, num

        end_x, full_num = extract_number(x)
        start_x, full_num = extract_number(end_x, forward=False)
        skip_x = (end_x - x) + 1
        return start_x, end_x, int(full_num), skip_x

    def is_symbol_adjacent(self) -> bool:
        for y in range(self.y - 1, self.y + 2):
            for x in range(self.start_x - 1, self.end_x + 2):
                if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
                    continue
                if data[y][x] in {"*", "=", "%", "#", "@", "&", "/", "$", "-", "+"}:
                    return True
        return False


def check_is_gear(loc_x: int, loc_y: int) -> (bool, int):
    digits = []
    for y in range(loc_y - 1, loc_y + 2):
        x = loc_x - 1
        while x < loc_x + 2:
            if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
                x += 1
                continue
            elif data[y][x].isdigit():
                number = FullNum(x, y)
                digits.append(number.val)
                x += number.skip_by - 1
            x += 1
    if len(digits) == 2:
        return True, digits[0] * digits[1]
    else:
        return False, 0


def part1():
    result = 0
    for y in range(len(data)):
        x = 0
        while x < len(data[y]):
            c = data[y][x]

            if c.isdigit():
                number = FullNum(x, y)
                x += number.skip_by - 1

                if number.is_symbol_adjacent():
                    result += number.val
            x += 1
    return result


def part2():
    result = 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            is_gear, ratio = check_is_gear(x, y)
            if c == "*" and is_gear:
                result += ratio
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
