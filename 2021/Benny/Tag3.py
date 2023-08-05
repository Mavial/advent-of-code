import requests
import os

# Import file and data
cookies = {"session":'53616c7465645f5ffe49539d296f6119885d578f2baedd651b9e3684b9005951301078d848a93de369ef07024d15b5a8'}
input = requests.get( "https://adventofcode.com/2021/day/3/input", cookies=cookies ).text.split("\n")[:-1]
gamma=[]

zwischenspeicher1=0
zwischenspeicher2=0
zwischenspeicher3=0
zwischenspeicher4=0
zwischenspeicher5=0
zwischenspeicher6=0
zwischenspeicher7=0
zwischenspeicher8=0
zwischenspeicher9=0
zwischenspeicher10=0
zwischenspeicher11=0
zwischenspeicher12=0
epsilon=[]
x=0
for i in input:
    if "1" == i[0]:
        zwischenspeicher1+=int(i[0])
        
    if "1" == i[1]:
        zwischenspeicher2+=int(i[1])
    if "1" == i[2]:
        zwischenspeicher3+=int(i[2])
    if "1" == i[3]:
        zwischenspeicher4+=int(i[3])
    if "1" == i[4]:
        zwischenspeicher5+=int(i[4])
    if "1" == i[5]:
        zwischenspeicher6+=int(i[5])
    if "1" == i[6]:
        zwischenspeicher7+=int(i[6])
    if "1" == i[7]:
        zwischenspeicher8+=int(i[7])
    if "1" == i[8]:
        zwischenspeicher9+=int(i[8])
    if "1" == i[9]:
        zwischenspeicher10+=int(i[9])
    if "1" == i[10]:
        zwischenspeicher11+=int(i[10])
    if "1" == i[11]:
        zwischenspeicher12+=int(i[11])

if zwischenspeicher1>500:
      gamma.append(1)
if zwischenspeicher1<500:
    gamma.append(0)
if zwischenspeicher2>500:
      gamma.append(1)
if zwischenspeicher2<500:
    gamma.append(0)
if zwischenspeicher3>500:
      gamma.append(1)
if zwischenspeicher3<500:
    gamma.append(0)
if zwischenspeicher4>500:
      gamma.append(1)
if zwischenspeicher4<500:
    gamma.append(0)
if zwischenspeicher5>500:
      gamma.append(1)
if zwischenspeicher5<500:
    gamma.append(0)
if zwischenspeicher6>500:
      gamma.append(1)
if zwischenspeicher6<500:
    gamma.append(0)
if zwischenspeicher7>500:
      gamma.append(1)
if zwischenspeicher7<500:
    gamma.append(0)
if zwischenspeicher8>500:
      gamma.append(1)
if zwischenspeicher8<500:
    gamma.append(0)
if zwischenspeicher9>500:
      gamma.append(1)
if zwischenspeicher9<500:
    gamma.append(0)
if zwischenspeicher10>500:
      gamma.append(1)
if zwischenspeicher10<500:
    gamma.append(0)
if zwischenspeicher11>500:
      gamma.append(1)
if zwischenspeicher11<500:
    gamma.append(0)
if zwischenspeicher12>500:
      gamma.append(1)
if zwischenspeicher12<500:
    gamma.append(0)



epsilon=[0,1,0,0,0,1,0,0,0,0,1,1]
print(gamma)

print(int(''.join(str(e) for e in gamma), 2) * int(''.join(str(e) for e in epsilon), 2))


#Teil 2

