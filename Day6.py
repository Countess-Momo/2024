import numpy as np
import math
import re

def Part1(Map, Case = 0):
    PathSize = Map.shape
    GuardLoc = np.where(Map == "^")
    #print("Part1 test", Map)
    #print(GuardLoc)
    GuardLoc = np.array([GuardLoc[0][0],GuardLoc[1][0]]) #Guards row and col
    Movements = [[-1,0],[0,1],[1,0],[0,-1]] #up,Right,down,right
    Heading = 0 #0 = up, 1 = right, 2 = down, 3 = left

    PathHistory = np.zeros([PathSize[0],PathSize[1],4], dtype=bool) #Keeps track of all locations visited with directions
    PathNotLooping = True

    while PathNotLooping:
        #Check location previously visited
        if PathHistory[GuardLoc[0],GuardLoc[1],Heading]: 
            break
        #Record Location

        PathHistory[GuardLoc[0],GuardLoc[1],Heading] = True
        Map[GuardLoc[0],GuardLoc[1]] = "X"
        
        #Check next location
        NextMove = GuardLoc + Movements[Heading]
        #Off Map
        if (min(NextMove) < 0) | (NextMove[0] >= PathSize[0]) | (NextMove[1] >= PathSize[1]):
            PathNotLooping = False; break
        #Wall
        elif Map[NextMove[0],NextMove[1]] == "#":
            Heading = (Heading + 1) % 4
        else: GuardLoc = NextMove
    if Case == 0:
        print(np.sum(Map == "X"))
        return np.where(Map == "X")
    else: 
        #print(PathNotLooping)
        return(PathNotLooping)


def Part2(Input,AllVisited):
    #FreshInput = np.array(Input)
    Changes = 0
    TotalNumTestCases = len(AllVisited[0])
    for i in range(TotalNumTestCases):
        if i % 128 == 0: print("{}% done".format(i/TotalNumTestCases))
        AltInput = np.array(Input)
        #print('Hi',AllVisited[0][i],AllVisited[1][i])
        if(AltInput[int(AllVisited[0][i]),AllVisited[1][i]] != '^'):
            AltInput[int(AllVisited[0][i]),AllVisited[1][i]] = '#'
        if(Part1(AltInput,1)): Changes += 1
    print(Changes)
    return Changes

def InputInitilization(Input):
    Input = re.sub("\n","",Input)
    Input = list(Input)
    Dim = int(math.sqrt(len(Input)))
    Input = np.array(Input)
    Input = np.reshape(Input,[Dim,Dim])
    return Input


with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input6.txt","r") as x:
    Input = x.read()

TInput = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

Input = InputInitilization(Input)
FreshInput = np.array(Input) ## IDK why scope isnt working. This is fucking dumb
print(Input)
AllVisited = Part1(Map=Input)
print(Input, FreshInput)
Part2(FreshInput,AllVisited)
