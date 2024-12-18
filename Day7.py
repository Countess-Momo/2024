import numpy as np
import re

def Part1(Input):
    Score = 0
    for i in range(len(Input)):
        OperationOptions = GenerateArrayOfBin(len(Input[i])-2)
        TestVal = Input[i][0]
        for OpTest in OperationOptions: #Testing each type of multiply and add
            ResultOfOperationSet = BiOpperateOnArray(Input[i],OpTest)
            if ResultOfOperationSet == TestVal:
                Score += TestVal
                break
    print(Score)
    return Score

def Part2(Input):
    Score = 0
    for i in range(len(Input)):
        OperationOptions = CountUpInNthBasetoMDigits(len(Input[i])-2,3)
        TestVal = Input[i][0]
        for OpTest in OperationOptions: #Testing each type of multiply and add
            ResultOfOperationSet = TriOpperateOnArray(Input[i],OpTest)
            if ResultOfOperationSet == TestVal:
                Score += TestVal
                break
    print(Score)
    return Score
def TriOpperateOnArray(Array,OperationsChoice):
    CurrentTotal = Array[1]
    for i in range(len(OperationsChoice)):
        if OperationsChoice[i] == 0: CurrentTotal += Array[i+2]
        elif OperationsChoice[i] == 1: CurrentTotal *= Array[i+2]
        else: CurrentTotal = int(str(CurrentTotal) + str(Array[i+2]))
    return CurrentTotal #Goal == CurrentTotal
def BiOpperateOnArray(Array,OperationsChoice):
    Goal = Array[0]
    CurrentTotal = Array[1]
    for i in range(len(OperationsChoice)):
        if(OperationsChoice[i]): CurrentTotal += Array[i+2]
        else: CurrentTotal *= Array[i+2]
    return CurrentTotal #Goal == CurrentTotal

def GenerateArrayOfBin(Length):
    Base = np.ones(Length, dtype=bool)
    All = np.ones((2**Length,Length), dtype=bool)
    i = 0
    Counter = 1
    while np.any(Base):
        if(Base[i]):
            Base[i] = False
            Base[0:i] = True
            All[Counter] = Base
            Counter +=1
            i = 0
        else: i += 1
    return All

def CountUpInNthBasetoMDigits(NumDigits,Base):
    
    Case = np.zeros(NumDigits)
    All = np.zeros(((Base**NumDigits),NumDigits))
    i = 0
    Counter = 1
    while Counter < Base**NumDigits:
        if(Case[i] < (Base)-1):
            Case[i] += 1
            Case[0:i] = 0
            All[Counter] = Case
            Counter +=1 # Keeps track of number of unique cases
            i = 0 #Rest looking position
        else: i += 1 #Move to next slot
    return All


def InputInitilization(Input):
    Input = Input.split('\n')
    for i in range (len(Input)):
        Input[i] = np.array(re.split(r':*\s', Input[i]), dtype=int)
    return Input


with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input7.txt","r") as x:
    Input = x.read()

TInput = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

Input = InputInitilization(Input)
#print(Input)
#print(GenerateArrayOfBin(5))
#print(CountUpInNthBasetoMDigits(3,3))
Part1(Input)
#28730327770375
Part2(Input)