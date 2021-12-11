import requests
import os
import numpy as np

# Import file and data
cookies = {"session": os.getenv("SESSION")}
input = [val for val in requests.get(
    "https://adventofcode.com/2021/day/5/input", cookies=cookies
).text.split("\n")][:-1]

input = [tuple(np.array([int(s) for s in num.split(",")])
               for num in coords.split(" -> ")) for coords in input]
np.seterr(divide='ignore', invalid='ignore')  # ignore divide by zero

"""Part 1"""
mem = {}
for points in input:
    if points[0][0] != points[1][0] and points[0][1] != points[1][1]:  # ignore if not vert or horiz
        continue

    vector = np.subtract(points[1], points[0])  # create vector between points
    # create unit vector for step size, round to  the nearest integer
    unit_vector = np.rint(np.divide(vector, np.linalg.norm(vector)))

    pos = np.array(points[0].astype(float))  # set start position
    finished = False
    while not finished:
        finished = np.array_equal(pos, points[1])
        if pos.__str__() in mem:
            mem[pos.__str__()] += 1
        else:
            mem[pos.__str__()] = 1
        # update position by adding unit vector
        pos = np.add(pos, unit_vector).astype(float)

print(len(list(filter(lambda x: x > 1, mem.values()))))


"""Part 2"""
mem = {}
for points in input:
    vector = np.subtract(points[1], points[0])  # create vector between points
    # create unit vector for step size, round to  the nearest integer
    unit_vector = np.rint(np.divide(vector, np.linalg.norm(vector)))

    pos = np.array(points[0].astype(int))  # set start position
    finished = False
    while not finished:
        finished = np.array_equal(pos, points[1])
        if pos.__str__() in mem:
            mem[pos.__str__()] += 1
        else:
            mem[pos.__str__()] = 1
        # update position by adding unit vector
        pos = np.add(pos, unit_vector).astype(int)

print(len(list(filter(lambda x: x > 1, mem.values()))))
