
def nextPermutation(nums):
    if len(nums)>0:
        tag=False
        for i in range(len(nums)-1,0,-1):
            if nums[i]> nums[i-1]:
                remainderList = nums[i:]
                remainderList.sort()
                for j in range(0,len(remainderList)):
                    if(remainderList[j]>nums[i-1]):
                        temp = remainderList[j]
                        remainderList[j] = nums[i-1]
                        nums[i-1] = temp
                        break
                remainderList.sort()
                for j in range(0,len(remainderList)):
                    nums[i+j] = remainderList[j]
                tag=True
                break
        if(tag==False):
            nums.sort()
    return nums

print(nextPermutation([1,2,5,5,6,4,3]))