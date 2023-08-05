import requests

cookies = {"session": "fill in here"}
input = requests.get('https://adventofcode.com/2021/day/2/input',
                     cookies=cookies).text.split('\n')[:-1]

"""Part 1"""
def Submarine1(input):
    depth, horizontal = 0,0
    for commands in input:
        command, value = commands[:-2], int(commands[-1:])
        if command == "forward":
            horizontal += value
        if command == "down":
            depth += value
        if command == "up":
            depth -= value

    return f"Depth of {depth} ; Horizontal value of {horizontal} ; Final result is {depth*horizontal}"

# Submarine1(input)

"""Part 2"""

def Submarine2(input):
    depth, horizontal, aim = 0,0,0
    for commands in input:
        command, value = commands[:-2], int(commands[-1:])
        if command == "forward":
            horizontal += value
            depth += aim*value
        if command == "down":
            aim += value
        if command == "up":
            aim -= value

    return f"Depth of {depth} ; Horizontal value of {horizontal} ; Final result is {depth*horizontal}"

# print(Submarine2(input))