import requests
import os

# Import file and data
cookies = {"session":'53616c7465645f5ffe49539d296f6119885d578f2baedd651b9e3684b9005951301078d848a93de369ef07024d15b5a8'}
input = requests.get( "https://adventofcode.com/2021/day/2/input", cookies=cookies ).text.split("\n")[:-1]
hor=0
ver=0
for i in input:
    a=i.split(" ")
    if "forward" in a:
     hor+=int(a[1])
    if "up" in a:
        ver-=int(a[1])
    if "down" in a:
         ver+=int(a[1])
print(hor*ver)

#Teil2
hor=0
ver=0
aim=0
for i in input:
    a=i.split(" ")
    if "forward" in a:
     hor+=int(a[1])
     ver+=aim*int(a[1])
    if "up" in a:
        aim-=int(a[1])
    if "down" in a:
         aim+=int(a[1])
    

print(hor*ver)