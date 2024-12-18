import numpy as np
import re 
def Part1(Input):
    Score = 0
    StringofInterest = ['X','M','A','S']
    Directions = [[-1,-1],[0,-1],[1,-1],
                  [-1,0] ,[0,0] ,[1,0],
                  [-1,1] ,[0,1] ,[1,1]]
    for i in range(len(Input)):
        for j, char in enumerate(Input[i]):
            if(char == StringofInterest[0]):
                for Move in Directions:
                    Score += DirectionTest(i,j,Move,1,Input, StringofInterest)
        print(Score)

        #XChecks = np.where(list(Input[i]) == StringofInterest[0])
        #print(XChecks)
    return

#Finds if a strign matches in a given direction of movment (only linear)
def DirectionTest(Row, Col,Move, Layer,Input, StringofInterest):
    NewRow = Row + Move[0]
    NewCol = Col + Move[1]
    if all([NewRow >= 0, NewCol >= 0, NewRow < len(Input), NewCol < len(Input[Col])]):
        if Input[NewRow][NewCol] == StringofInterest[Layer]:
            if Layer >= (len(StringofInterest) - 1): # one less because that is end of line
                return(True)
            else: return DirectionTest(NewRow,NewCol,Move,Layer+1,Input,StringofInterest)
    return False


def Part2(Input):
    Score = 0
    StringofInterest = ['A','M','S']
    DirectionA = [[-1,-1], [1,1]] #moving by the four corners
    DirectionB = [[1,-1],[-1,1]]
    for i in range(len(Input)):
    #for i in [4]:
        #f i > 1: break
        for j, char in enumerate(Input[i]):
            if(char == StringofInterest[0]):
                ASlash = False
                BSlash = False
                for Move in DirectionA:
                    ASlash = ASlash | XTest(i,j,Move,1,Input, StringofInterest)
                for Move in DirectionB:
                    BSlash =  BSlash| XTest(i,j,Move,1,Input, StringofInterest)
                print(ASlash, BSlash)
                if ASlash & BSlash: Score += 1
    print(Score)

        #XChecks = np.where(list(Input[i]) == StringofInterest[0])
        #print(XChecks)
    return

#Finds if a strign matches in a given direction an x, bad function not reusable
def XTest(Row, Col,Move, Layer,Input, StringofInterest):
    print('We here')
    NewRow = Row + Move[0] * (-1)**Layer * Layer  #Base position, rotate which side to extend by each layer, and scales by layer
    NewCol = Col + Move[1] * (-1)**Layer * Layer
    #print(NewRow,"=", Row,"+", Move[0],(-1)**Layer, Layer)
    #print(NewCol,"=", Col,"+", Move[1],(-1)**Layer, Layer)
    if all([NewRow >= 0, NewCol >= 0, NewRow < len(Input), NewCol < len(Input[Col])]):
        #print(Row,Move[0],-1**Layer * Layer,NewRow)
        #print(Input[NewRow][NewCol], StringofInterest[Layer])
        if Input[NewRow][NewCol] == StringofInterest[Layer]:
            #print(Layer, len(StringofInterest))
            if Layer >= (len(StringofInterest) - 1): # one less because that is end of line
                return(True)
            else:
                #print('NextLayer') 
                return XTest(NewRow,NewCol,Move,Layer+1,Input,StringofInterest)
    return False
with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input4.txt","r") as x:
    Input = x.read()
    Input = np.array( Input.split("\n"))



#Part1(Input)
Part2(Input)

#XTest(7, 1,[-1,-1], 1,Input, ['A','M','S'])