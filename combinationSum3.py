import copy


def recursive(iteration,k,currentValue,currentList,ansList,actualValue):
    if sum(currentList)>actualValue:
        return
    if len(currentList) == k and sum(currentList)==actualValue:
        currentList.sort()
        if currentList not in ansList:
            ansList.append(currentList)
        return
    if len(currentList)==k:
        return
    for i in range(1,10):
        currentValue = currentValue-i
        if i not in currentList:
            currentList.append(i)
            recursive(i,k,currentValue,copy.deepcopy(currentList),ansList,actualValue)
            currentList = currentList[:-1]

def combinationSum3(k,n):
    ansList=[]
    recursive(0,k,n,[],ansList,n)
    print(ansList)

combinationSum3(9,45)