import numpy as np

def Day1_2024(Input):
    
    Checkpoints = len(Input)

    Left_Array = np.zeros(Checkpoints)
    Right_Array = np.zeros(Checkpoints)

    for i in range(Checkpoints):
        Val = Input[i].split("   ")
        Left_Array[i] = int(Val[0])
        Right_Array[i] = int(Val[1])
    
    Left_Array = np.sort(Left_Array)
    Right_Array = np.sort(Right_Array)

    TotalScore = abs(sum(Left_Array - Right_Array))

    print(TotalScore)
    return TotalScore

def Day1_2024_2(Input):
    
    Checkpoints = len(Input)

    Left_Array = np.zeros(Checkpoints)
    Right_Array = np.zeros(Checkpoints)

    for i in range(Checkpoints):
        Val = Input[i].split("   ")
        Left_Array[i] = int(Val[0])
        Right_Array[i] = int(Val[1])

    TotalScore = 0
    for i in range(Checkpoints):
        CheckVal = Left_Array[i]
        InstancesOfOccur = sum(Right_Array == Left_Array[i])
        AddScore = Left_Array[i] * sum(Right_Array == Left_Array[i])
        TotalScore += CheckVal * InstancesOfOccur

    print(TotalScore)
    return TotalScore


with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input1.txt","r") as x:
    Input = x.read()
    Input = Input.split("\n")

#Input = ['3   4','4   3','2   5','1   3','3   9',"3   3"]


Day1_2024(Input)
Day1_2024_2(Input)