import requests
import os

# Import file and data
cookies = {"session": os.getenv('SESSION')}
input = requests.get( "https://adventofcode.com/2021/day/2/input", cookies=cookies ).text.split("\n")[:-1]

"""PART 1"""
x,y = 0,0
for move in input:
    match move[:-2]:
        case "forward": x+=int(move[-1:])
        case "down": y+=int(move[-1:])
        case "up": y-=int(move[-1:])
print(x*y)

"""PART 2"""
x,y,aim = 0,0,0
for move in input:
    match move[:-2]:
        case "forward": x, y = x + int(move[-1:]), y + aim*int(move[-1:])
        case "down": aim += int(move[-1:])
        case "up": aim -= int(move[-1:])
print(x*y)