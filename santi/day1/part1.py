import requests
import os

# Import file and data
cookies = {"session": os.getenv('SESSION')}
input = requests.get('https://adventofcode.com/2021/day/1/input',
                     cookies=cookies).text.split('\n')[:-1]

# Solution
print(len([meas for index, meas in enumerate(input) if int(meas) > int(input[index-1])]))

# Alternative solution (Benny)
solution = 0
for index in range(1, len(input)):
    if int(input[index-1]) < int(input[index]):
        solution += 1
print(solution)