
def hasMaximumValue(ansArray:[],cadidateElement):
    for i in range(0,len(ansArray)):
        if ansArray[i] > cadidateElement:
            return True
    return False

def isAddable(candidateElement,ansArray,candidates):
    ansArrayCount=0
    candidatesCount=0
    for i in range(0,len(ansArray)):
        if ansArray[i]==candidateElement:
            ansArrayCount+=1
    for i in range(0,len(candidates)):
        if candidates[i]==candidateElement:
            candidatesCount+=1
    if ansArrayCount< candidatesCount:
        return True
    else: return False

def recursivelyCount(candidates,target,ansArray:[],totalArray):
    sumValue = sum(ansArray)
    if sumValue > target:
        return ansArray

    if sumValue == target:
        totalArray.append(ansArray)
        return ansArray

    for i in range(0,len(candidates)):
        if hasMaximumValue(ansArray,candidates[i])!=True and isAddable(candidates[i],ansArray,candidates):
            sumValue+=candidates[i]
            ansArray.append(candidates[i])
            ansArray = recursivelyCount(candidates,target,ansArray,totalArray)
            ansArray = ansArray[:len(ansArray)-1]
    return ansArray

def combinationSum(candidates, target):
    candidates.sort()
    totalArray=[]
    print(recursivelyCount(candidates,target,[],totalArray))
    totalArray = list(set(map(tuple,totalArray)))
    ans=[]
    for i in range(0,len(totalArray)):
        ans.append(list(totalArray[i]))
    return ans

print(combinationSum([23,32,22,19,29,15,11,26,28,20,34,5,34,7,28,33,30,30,16,33,8,15,28,26,17,10,25,12,6,17,30,16,6,10,23,22,20,29,14,5,6,5,5,6,29,20,34,24,16,7,22,11,17,7,33,21,13,15,29,6,19,16,10,21,21,28,8,6]
,27))
