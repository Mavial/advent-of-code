import requests
import os

# Import file and data
cookies = {"session": os.getenv("SESSION")}
input = [int(val) for val in requests.get(
    "https://adventofcode.com/2021/day/7/input", cookies=cookies
).text.removesuffix("\n").split(",")]


"""Part 1"""

lowest_cons = 0
amount_tracker = [i for i in enumerate([input.count(i) for i in range(
    max(input)+1)]) if i[1] > 0]  # (horiz_pos, amount)
for selected_position in amount_tracker:
    cons = 0
    for hor_pos in amount_tracker:
        cons += abs(hor_pos[0]-selected_position[0]) * hor_pos[1]
    if lowest_cons > cons or lowest_cons == 0: lowest_cons = cons

print(lowest_cons)

"""Part 2"""

lowest_cons = 0
amount_tracker = [i for i in enumerate([input.count(i) for i in range(
    max(input)+1)]) if i[1] > 0]  # (horiz_pos, amount)
for selected_position in amount_tracker:
    cons = 0
    for hor_pos in amount_tracker:
        dist = abs(hor_pos[0]-selected_position[0])
        cons += int((dist**2+dist)/2 * hor_pos[1])
    if lowest_cons > cons or lowest_cons == 0: lowest_cons = cons

print(lowest_cons)
