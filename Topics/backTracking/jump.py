def jump(nums):
    numsLength = len(nums)
    jumpArray = [0]* numsLength
    for i in range(0,numsLength):
        count = jumpArray[i] + 1
        for j in range(i+1,i+nums[i]+1):
            if j < numsLength and jumpArray[j] !=0 and jumpArray[j]> count:
                jumpArray[j] = count
            if j < numsLength and jumpArray[j] == 0:
                jumpArray[j] = count
    return jumpArray[numsLength-1]
print(jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))