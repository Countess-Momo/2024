import re

def Part1(Input):
    RealCases = re.findall(r"mul\(\d{1,3},\d{1,3}\)", Input)

    TotalScore = 0
    for i in RealCases:
        SingleCase = re.split(r"mul\(|,|\)",i)
        TotalScore += int(SingleCase[1])*int(SingleCase[2])
    print(TotalScore)


    return TotalScore

def Part2(Input):
    RealCases = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", Input)

    TotalScore = 0
    DoMultiply = True
    for i in RealCases:
        if( i == "don't()"): DoMultiply = False
        elif(i == "do()"): DoMultiply = True
        elif(DoMultiply):
            SingleCase = re.split(r"mul\(|,|\)",i)
            TotalScore += int(SingleCase[1])*int(SingleCase[2])
    print(TotalScore)


    return TotalScore

with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input3.txt","r") as x:
    Input = x.read()

#Input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#print(Input)
Part1(Input)
Part2(Input)
#print(re.split(r"mul|,",Input))