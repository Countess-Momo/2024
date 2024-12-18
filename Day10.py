import numpy as np
import re

def Part1(Input):
    print(np.where(Input == 0))
    return

def Part2(Input):
    return

def InputInitilization(Input):
    Lines = len(re.findall(r'\n', Input))+1
    Input = re.sub('\n','',Input)
    print(Lines)
    Input = np.array(list(Input)).reshape(Lines,Lines)
    return Input


def main():

    with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input10.txt","r") as x:
        Input = x.read()
    
    Input = InputInitilization(Input)
    print(Input)
    Part1(Input)
    return


main()