import re
import numpy as np

def Part1(Input):
    Frequencies = np.unique(Input)[1:]
    AntiNodes = np.zeros_like(Input, dtype = int)
    for CheckFreq in Frequencies:
        Nodes = np.where(Input == CheckFreq)
        NodeNum = len(Nodes[0])
        for i in range(NodeNum-1):
            for j in range(i+1,NodeNum):
                NewNodes = FindAntiNodes(np.array([Nodes[0][i],Nodes[1][i]]),
                                    np.array([Nodes[0][j],Nodes[1][j]]),
                                    Input.shape[0],Input.shape[1])
                for NewNode in NewNodes:
                    AntiNodes[NewNode[0],NewNode[1]] = 1
                    if(Input[NewNode[0],NewNode[1]] == "."):
                        Input[NewNode[0],NewNode[1]] = "#"
    #print(Input)
    #print(AntiNodes)
    print(np.sum(AntiNodes))
    #print(len(np.where(Input == "#")[0]))
    return

def Part2(Input):
    RowMax = Input.shape[0]
    ColMax = Input.shape[1]
    Frequencies = np.unique(Input)[1:]
    AntiNodes = np.zeros_like(Input, dtype = int)
    for CheckFreq in Frequencies:
        Nodes = np.where(Input == CheckFreq)
        #print(Nodes)
        NodeNum = len(Nodes[0])
        for i in range(NodeNum-1):
            for j in range(i+1,NodeNum):
                A = np.array([Nodes[0][i],Nodes[1][i]])
                B = np.array([Nodes[0][j],Nodes[1][j]])
                Diff = A - B
                #A = np.array(A + Diff)
                while all(A >= 0) & (A[0] < RowMax) & (A[1] < ColMax):
                    AntiNodes[A[0],A[1]] = 1
                    if(Input[A[0],A[1]] == "."):
                        Input[A[0],A[1]] = "#"
                    A = A + Diff
                #B = np.array(B - Diff)
                while all(B >= 0) & (B[0] < RowMax) & (B[1] < ColMax):
                    AntiNodes[B[0],B[1]] = 1
                    if(Input[B[0],B[1]] == "."):
                        Input[B[0],B[1]] = "#"
                    B = B - Diff
    #print(Input)
    #print(AntiNodes)
    print(np.sum(AntiNodes))
    #print(len(np.where(Input == "#")[0]))
    return

def FindAntiNodes(A,B,RowMax = 50,ColMax=50):
    Diff = A - B
    AntiNodes = np.array([A + Diff,B - Diff])
    i = 0
    while i < len(AntiNodes):
        if any(AntiNodes[i] < 0)| (AntiNodes[i][0] >= RowMax) | (AntiNodes[i][1] >= ColMax):
            AntiNodes = np.delete(AntiNodes,i,0)
        else: i += 1
    return AntiNodes


def InputInitilization(Input):
    Lines = len(re.findall(r'\n', Input))+1
    Input = re.sub('\n','',Input)
    Input = np.array(list(Input)).reshape(Lines,Lines)
    return Input

with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input08.txt","r") as x:
    Input = x.read()

TInput = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

AInput = '''T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........'''

Input = InputInitilization(Input)

print('Part1')
Part1(np.array(Input))
print('Part2')
Part2(Input)