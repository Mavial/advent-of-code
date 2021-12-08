import requests
import os
import copy

from requests.api import request

# Import file and data
cookies = {"session": os.getenv("SESSION")}
input = requests.get(
    "https://adventofcode.com/2021/day/3/input", cookies=cookies
).text.split("\n")[:-1]

"""Part 1"""
total = [0 for _ in range(12)]
for row in input:
    total = [sum(tup) for tup in list(zip(total, [int(b) for b in row]))]

gamma, epsilon = list(map(lambda x: 1 if x > len(input) / 2 else 0, total)
                      ), list(map(lambda x: 0 if x > len(input) / 2 else 1, total))
print(int(''.join(str(e) for e in gamma), 2) *
      int(''.join(str(e) for e in epsilon), 2))

"""Part 2"""
res = 1

def get_del_val(sum_val, pref_val):
    if sum_val == len(input_copy) / 2:
        return str(int(not pref_val))
    return str(int(sum_val > len(input_copy) / 2)) if pref_val == 0 else str(int(sum_val < len(input_copy) / 2))

for pref_val in range(2):
    input_copy = copy.copy(input)
    for i in range(len(input_copy[0])):
        del_val = get_del_val(
            sum(map(lambda x: int(x[i]), input_copy)), pref_val)
        input_copy = list(filter(lambda x: x[i] != del_val, input_copy))
        if len(input_copy) == 1: break
    res *= int(''.join(str(e) for e in input_copy[0]), 2)

print(res)
