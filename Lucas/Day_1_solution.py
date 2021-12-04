import requests

cookies = {"session": "fill in here"}
input = requests.get('https://adventofcode.com/2021/day/1/input',
                     cookies=cookies).text.split('\n')[:-1]

print(sum(1 for i in range(1,len(input)) if int(input[i-1]) < int(input[i])))
the_list = [int(input[i])+int(input[i-1])+int(input[i-2]) for i in range(2,len(input))]
print(sum(1 for i in range(1,len(the_list)) if the_list[i-1] < the_list[i]))