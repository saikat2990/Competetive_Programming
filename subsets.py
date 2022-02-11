
def backTrack(nums,ansList,tempList,target):
    if list(tempList) not in ansList:
        ansList.append(list(tempList))
    for i in range(target,len(nums)):
        tempList.append(nums[i])
        tempList.sort()
        backTrack(nums,ansList,tempList.copy(),i+1)
        tempList.pop()

def subsets(nums):
        ansList=[]
        nums.sort()
        backTrack(nums,ansList, [], 0)
        return ansList

print(subsets([1,2,3,3]))
print(subsets([4,1,0]))
