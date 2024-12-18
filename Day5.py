import numpy as np
def Part1(Rules,Updates):
    Score = 0
    for UpdateCase in Updates:
        ValidUpdate = True
        for j in range(len(UpdateCase)): #Skip the first trivial case

            PriorUpdates = Rules[Rules[:,1] == UpdateCase[j],0]
            if any(np.isin(PriorUpdates, UpdateCase[j:])): #Checks if any prior updates occur after the test case
                ValidUpdate = False
                break
        if ValidUpdate:
            Score += UpdateCase[int(len(UpdateCase)/2)]
    print(Score)
    return(Score)

def Part2(Rules,Updates):
    Score = 0
    for UpdateCase in Updates:
        NewCase = UpdateCase
        j = 0

        CaseWouldHaveFailed = False
        while j < len(NewCase):
            #Logic for changes:
            #Go untill one point fails, when point fails, move first fail point to one position before it, Run again at ne inserted point+0hj
            PriorUpdates = Rules[Rules[:,1] == NewCase[j],0]
            FailCase = np.where(np.isin(NewCase[j:], PriorUpdates))[0] #The array of indexes for wichi an element would need to be moved
            if len(FailCase) > 0: #Checks if any prior updates occur after the test case
                CaseWouldHaveFailed = True                
                print(FailCase)
                ElementHold = NewCase[j] #Holding val for element swaping
                NewCase[j] = NewCase[FailCase[0] + j]
                NewCase[FailCase[0] + j] = ElementHold
            else: j += 1
        print(NewCase,UpdateCase)
        if CaseWouldHaveFailed: #checking to see if change was made, then include it
            Score += NewCase[int(len(NewCase)/2)]
    print(Score)
    return

#Takes the input for Day 5 and transformes it into two 2-d arrays, one rules and one updates
def StringInitilizer(Input):
    Input = Input.split('\n\n')
    Rules, Updates = Input
    #Setting up the Rules section
    Rules = Rules.split("\n")
    for i in range(len(Rules)):
        Rules[i] = np.array(Rules[i].split("|"), dtype = int)
    Rules = np.array(Rules)
    Updates = Updates.split("\n")
    #Setting up the updates section
    for i in range(len(Updates)):
        Updates[i] = np.array(Updates[i].split(","), dtype = int)
    return[Rules,Updates]

def OrderRules(Rules):#Unused, To much effort
    LeftOnly =  Rules[np.isin(Rules[:,0], Rules[:,1], invert=True),0]
    RightOnly = Rules[np.isin(Rules[:,1], Rules[:,0], invert=True),1]
    print(LeftOnly,RightOnly)

with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input5.txt","r") as x:
    Input = x.read()
    #Input = Input.split("\n")

TInput = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,97,47,61,53
75,47,61,53,29
97,61,53,29,13
75,29,13
61,13,29
97,13,75,29,47'''

Rules, Updates = StringInitilizer(Input)
#Part1(Rules, Updates)
Part2(Rules, Updates)
