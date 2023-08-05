import requests
import os

# Import file and data
cookies = {"session": ""}
input = [ int(num) for num in requests.get( "https://adventofcode.com/2021/day/1/input", cookies=cookies ).text.split("\n")[:-1] ]


ergebnis=0

for index in range(len(input)-1):
    
    if input[index+1]>input[index]:
        ergebnis+=1
    

print(ergebnis)
    
#Teil2

ergebnis2=0
for index in range(len(input)-3):
    if  input[index] + input[index+1] + input[index+2]<input[index+1] + input[index+2] + input[index+3]:
        ergebnis2+=1

print(ergebnis2)