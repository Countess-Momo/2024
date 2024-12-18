import numpy as np

def Part1(Input):
    SafeCases = 0
    for i in range(len(Input)):
        Case = np.array(Input[i].split(" "), dtype = np.int16)
        SafeCases += CaseCheck(Case)
    print(SafeCases)
    return
def Part2(Input):
    SafeCases = 0
    for i in range(len(Input)):
        Case = np.array(Input[i].split(" "), dtype = np.int16)
        AllSafe = CaseCheck(Case)
        if AllSafe:
            SafeCases+=1
        else:
            print(Case)
            for j in range(len(Case)):
                TempCase = Case
                TempCase = np.delete(TempCase,j)
                if CaseCheck(TempCase):
                   SafeCases +=1
                   break
    print(SafeCases)
    return

def CaseCheck(Case):
        Diff = Case[:-1] - Case[1:]
        return all([all(abs(Diff) <= 3),
                          any([all(abs(Diff)==Diff),all(abs(Diff)==-Diff)]),
                          all(Diff != 0)])
with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input2.txt","r") as x:
    Input = x.read()
    Input = Input.split("\n")

Part1(Input)
Part2(Input)
