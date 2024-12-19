import numpy as np
import re

def Part1(Map):
    MaxRow, MaxCol = np.shape(Map)
    TrailHeads = np.array(np.where(Map == 0))
    TrailEnds = (np.array(np.where(Map == 9)))
    EndScore = np.zeros(len(TrailEnds[0]),dtype=bool)
    Score = 0

    for i in range(len(TrailHeads[0])):
        Score += np.sum(FindTrailEnds(Map,TrailHeads[0:,i],MaxRow, MaxCol,TrailEnds,EndScore = np.array(EndScore)))
    print(Score)
    return Score

def FindTrailEnds(Map,Position, MaxRow, MaxCol,TrailEnds,EndScore):
    Movements = [[-1,0],[0,1],[1,0],[0,-1]] #up,Right,down,left
    for Move in Movements:
        TestPos = Position + Move
        if IsOnMap(TestPos,MaxRow,MaxCol): #Make sure Testpoint is on the map
            if Map[TestPos[0],TestPos[1]] == (Map[Position[0],Position[1]]+1): 
                if Map[TestPos[0],TestPos[1]] == 9: #End of trail
                    EndScore[np.where((TrailEnds[0,:] == TestPos[0]) & (TrailEnds[1,:]==TestPos[1]))[0]] = 1
                EndScore =  FindTrailEnds(Map,TestPos, MaxRow, MaxCol,TrailEnds,EndScore)
    return EndScore

def IsOnMap(Position,MaxRow,MaxCol): #Simple function to improve redability
    return (min(Position) >= 0) & (Position[0] < MaxRow) & (Position[1] < MaxCol)
def Part2(Map):
    MaxRow, MaxCol = np.shape(Map)
    TrailHeads = np.array(np.where(Map == 0))
    Score = 0
    
    for i in range(len(TrailHeads[0])):
        Score += np.sum(FindAllTrails(Map,TrailHeads[0:,i],MaxRow, MaxCol))
    print(Score)
    return Score

def FindAllTrails(Map,Position, MaxRow, MaxCol):
    Movements = [[-1,0],[0,1],[1,0],[0,-1]] #up,Right,down,left
    Score = 0
    #print(Position)
    for Move in Movements:
        TestPos = Position + Move
        if IsOnMap(TestPos,MaxRow,MaxCol): #Make sure Testpoint is on the map
            #print('current:', (Map[Position[0],Position[1]]), "Test:", Map[TestPos[0],TestPos[1]],)
            if Map[TestPos[0],TestPos[1]] == (Map[Position[0],Position[1]]+1): 
                if Map[TestPos[0],TestPos[1]] == 9: #End of trail
                    Score += 1
                else: Score +=  FindAllTrails(Map,TestPos, MaxRow, MaxCol)
    return Score

def InputInitilization(Input):
    Lines = len(re.findall(r'\n', Input))+1
    Input = re.sub('\n|\s','',Input)
    Input = np.array(list(Input)).reshape(Lines,Lines)
    Input = Input.astype(int)
    return Input


def main():

    with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input10.txt","r") as x:
        Input = x.read()
    AInput = '''0123
    5654
    5789
    2222'''
    TInput = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
    Input = InputInitilization(Input)
    Part1(Input)
    Part2(Map = Input)
    return


main()