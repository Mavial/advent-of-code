import requests
import os
import numpy as np

# Import file and data
cookies = {"session": os.getenv("SESSION")}
input = [int(val) for val in requests.get(
    "https://adventofcode.com/2021/day/6/input", cookies=cookies
).text.removesuffix("\n").split(",")]

# input = [3, 4, 3, 1, 2]  # test input

"""Part 1 & 2"""


def main(input, days):
    f_tracker = [input.count(i) for i in range(9)]
    for _ in range(days):
        f_tracker.append(0)
        if f_tracker[0] > 0:
            f_tracker[7] += f_tracker[0]
            f_tracker[9] = f_tracker[0]
        del f_tracker[0]
    return sum(f_tracker)


print(main(input, 80))
print(main(input, 256))
