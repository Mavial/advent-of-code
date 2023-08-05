import requests

cookies = {"session": "fill in here"}
input = requests.get('https://adventofcode.com/2021/day/3/input',
                     cookies=cookies).text.split('\n')[:-1]

"""Part 1"""
def power_consumption(input):
    gamma_rate = ""
    for i in range(len(input[0])):
        counter = [input[j][i] for j in range(len(input))]
        print(counter)
        if counter.count("0") > counter.count("1"):
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    epsilon_rate = ''.join(['1' if i == '0' else '0'
                     for i in gamma_rate])
    return f"Power consumption is {int(gamma_rate,2)*int(epsilon_rate,2)}"

# print(power_consumption(input))

"""Part 2"""
new_input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
def life_support(input):
    oxygen_rating, CO2_rating = input, input
    for i in range(len(input[0])):
        if len(oxygen_rating) > 1:
            counter = [oxygen_rating[j][i] for j in range(len(oxygen_rating))]

            if counter.count("1") >= counter.count("0"):
                oxygen_rating = [oxygen_rating[k] for k in range(len(counter)) if counter[k] == "1"]

            else: #if more 0's than 1's
                oxygen_rating = [oxygen_rating[l] for l in range(len(counter)) if counter[l] == "0"]
        else:
            break

    ### Split the oxygen and CO2 ratings as both depended on a counter themselves depending on the length of either the oxygen or CO2 lists; TLDR : it was easier to split them, both in terms of readability and difficulty
    
    for x in range(len(input[0])):
        if len(CO2_rating) > 1:
            counter2 = [CO2_rating[j][x] for j in range(len(CO2_rating))]
            if counter2.count("1") >= counter2.count("0"):
                CO2_rating = [CO2_rating[m] for m in range(len(counter2)) if counter2[m] == "0"]
            else:
                CO2_rating = [CO2_rating[w] for w in range(len(counter2)) if counter2[w] == "1"]
        else:
            break

    return f"Oxygen : {oxygen_rating[0]} ; CO2 : {CO2_rating[0]} ; final is : {int(oxygen_rating[0],2)*int(CO2_rating[0],2)}"

print(life_support(input))

