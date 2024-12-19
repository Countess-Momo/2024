
import numpy as np
def Part1(Input):
    MaxID = int(len(Input)/2)
    
    #Trackers for the Lower side of the data tracker
    LowID = 0
    LowReps = int(Input[0])

    #Trackers for the upper side of the data tracker
    TopID = MaxID
    TopReps = int(Input[TopID*2])

    Score = 0
    Is_File = True
    #PositionAdd = 0
    #ProdElements = np.zeros(2, dtype=int)
    IndexPoint = 0# the index of each element in storage
    i = 0 #The index we are evaluating in the compressed format
    CountDown = -1
    while TopID >= LowID:
        if(TopID == LowID):
            CountDown = TopReps # when low and top share a point, this keeps them on the same tracker
        SpaceReps = int(Input[i])
        if (i % 2) == 0: #This is for a file case, we add each file into position
            for j in range(int(Input[i])):
                Score += LowID * IndexPoint
                #print(LowID * IndexPoint)
                CountDown = CountDown -1 #Irelevant untill TopID = LoqID   
                if CountDown == 0: break   
                IndexPoint += 1
            LowID = LowID + 1
        elif (i % 2) == 1: # Case for empty file
            for j in range(int(Input[i])):
                Score += TopID * IndexPoint
                #print(TopID * IndexPoint)
                IndexPoint += 1 #Track next index for multiplication
                TopReps = TopReps - 1 #Track next top side to add to blank.
                CountDown = CountDown -1 #Irelevant untill TopID = LoqID   
                if CountDown == 0: break 
                if TopReps == 0: #When you have run out of top reps
                    TopID = TopID - 1
                    print(Input[TopID*2])
                    print('hi')
                    TopReps = int(Input[TopID*2])
        if CountDown == 0: break
        i += 1
    print(Score)       

    return Score

def Part2(Input):
    NotStoredFiles = np.arange(int(len(Input)/2)+1) #Array of all the file numbers of fiels not in our storage system
    Score = 0

    IndexPoint = 0# the index of each element in storage
    i = 0 #The index we are evaluating in the compressed format

    CountDown = -1
    while len(NotStoredFiles) > 0:
        SpaceReps = int(Input[i])
        if (i % 2) == 0: #This is for a file case, we add each file into position
            #print(i/2)
            if not np.isin(int(i/2), NotStoredFiles):
                IndexPoint += SpaceReps
            else:
                for j in range(int(Input[i])):
                    Score += NotStoredFiles[0] * IndexPoint #Mukltiplies file number by storage index
                    #print(NotStoredFiles[0] * IndexPoint)
                    IndexPoint += 1
                NotStoredFiles = np.delete(NotStoredFiles,0) # once a file is stored, its file number is removed from the list
        elif (i % 2) == 1: # Case for empty file
            bigbreak = False
            if(Input[i+1]=='0'):
                print('Doublegap')
            while SpaceReps > 0:
                TopInsert = len(NotStoredFiles)-1
                if TopInsert < 0: break
                while int(Input[NotStoredFiles[TopInsert]*2]) > SpaceReps: #find if a highest file num will fit
                    TopInsert = TopInsert - 1
                    if((i / 2) >NotStoredFiles[TopInsert])|(TopInsert <0) : 
                        if (Input[i+1] != '0'):
                            bigbreak = True
                            break
                        i += 2 #Skips the next file (Since blank)
                        SpaceReps += int(Input[i]) #adds additional gaps to spacereps
                if(bigbreak): 
                    IndexPoint = IndexPoint + SpaceReps
                    break
                for j in range(int(Input[NotStoredFiles[TopInsert]*2])):
                    Score += NotStoredFiles[TopInsert] * IndexPoint #File Num times Position
                    #print(NotStoredFiles[TopInsert] * IndexPoint)
                    IndexPoint += 1 #Track next index for multiplication
                    #print(Input[TopInsert*2])
                    SpaceReps = SpaceReps - 1
                NotStoredFiles = np.delete(NotStoredFiles,TopInsert) # once a file is stored, its file number is removed from the list

        i += 1
    print(Score)       

    return Score

def Part1Er(Input):
    MaxID = int(len(Input)/2)
    print(MaxID)
    
    #Trackers for the Lower side of the data tracker
    LowID = 0
    LowReps = int(Input[0])

    #Trackers for the upper side of the data tracker
    TopID = MaxID
    TopReps = int(Input[TopID*2])

    Score = 0
    Is_File = True
    PositionAdd = 0
    ProdElements = np.zeros(2, dtype=int)
    for i in range(len(Input)):
        SpaceReps = int(Input[i])
        if (i % 2) == 0: #This is for a file case, we add each file into position
            for j in range(int(Input[i])):

                ProdElements[PositionAdd] = LowID
                if PositionAdd == 1: Score += np.prod(ProdElements) #When both elements are full, Score increases by their product
                PositionAdd = (PositionAdd + 1) % 2 #Swap next input location
            LowID = LowID + 1
        elif (i % 2) == 1: # Case for empty file
            for j in range(int(Input[i])):
                ProdElements[PositionAdd] = TopID
                TopReps = TopReps - 1
                if TopReps == 0: #When you have run out of top reps
                    TopID = TopID - 1
                    TopReps = int(Input[TopID*2])
                if PositionAdd == 1: Score += np.prod(ProdElements) #When both elements are full, Score increases by their product
                PositionAdd = (PositionAdd + 1) % 2 #Swap next input location
    print(Score)       

    return Score

def Main():
    with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\2024\\Input09.txt","r") as x:
        Input = x.read()
    TInput = "2333133121414131402"
    AInput = "2033133121414131402"
    BInput = '1313165' #169 
    CInput = '99538772941' #2834, Should be 5768
    DInput = '12101'
    #Part1(Input)
    Part2(Input)
    #6379678017108 = too high
    #6379678017108 = too high
    #6379677752410

Main()