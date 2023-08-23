import operator
from collections import deque
from typing import List, Callable, Deque
from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=11)
    raw_data = data_loader.load()
    raw_monkeys = raw_data.split("\n\n")

    monkeys = [
        [line.strip().split() for line in monkey.splitlines()] for monkey in raw_monkeys
    ]

    return monkeys


class Monkey:
    monkeys: List["Monkey"] = []

    def __init__(
        self, raw_starting_items: str, raw_operation: str, raw_test: List[str]
    ):
        self._items_held: Deque[int] = self._parse_starting_items(raw_starting_items)
        self._operation: Callable[[int], int] = self._parse_operation(raw_operation)
        self._test: Callable = self._parse_test(raw_test)
        self.items_inspected = 0
        Monkey.monkeys.append(self)

    def _parse_starting_items(self, raw_starting_items: str) -> Deque[int]:
        return deque(int(n.replace(",", "")) for n in raw_starting_items[2:])

    def _parse_operation(self, raw_operation: str) -> Callable[[int], int]:
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        return lambda old: ops[raw_operation[4]](
            int(raw_operation[3]) if raw_operation[3] != "old" else old,
            int(raw_operation[5]) if raw_operation[5] != "old" else old,
        )

    def _parse_test(self, raw_test: List[str]) -> Callable[[int], int]:
        divisor = int(raw_test[0][3])
        test_pass = int(raw_test[1][5])
        test_fail = int(raw_test[2][5])
        return lambda x: test_pass if x % divisor == 0 else test_fail

    def add_item(self, item: int):
        self._items_held.append(item)

    def turn(self):
        while self._items_held:
            item = self._items_held.popleft()

            self.items_inspected += 1

            new_item_value = int(self._operation(item) / 3)
            new_monkey = self._test(new_item_value)

            self.monkeys[new_monkey].add_item(new_item_value)


def parse_data(data: List[str]) -> List[Monkey]:
    for raw_monkey in data:
        Monkey(
            raw_starting_items=raw_monkey[1],
            raw_operation=raw_monkey[2],
            raw_test=raw_monkey[3:],
        )

    return Monkey.monkeys


unparsed_data = load_data()
data = parse_data(unparsed_data)


def part1():
    for _ in range(20):
        for monkey in data:
            monkey.turn()
    items_inspected_list = [monkey.items_inspected for monkey in data]

    highest_items_inspected = max(items_inspected_list)
    items_inspected_list.remove(highest_items_inspected)
    second_highest_items_inspected = max(items_inspected_list)

    return highest_items_inspected * second_highest_items_inspected


if __name__ == "__main__":
    print(part1())
