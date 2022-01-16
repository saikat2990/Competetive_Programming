def sortColors(nums:[]):
    zerosLastCount=0
    onesLastCount=0
    twoLastCount=0
    for i in range(0,len(nums)):
        if(nums[i]==0):
            zerosLastCount+=1

        if(nums[i]==1): onesLastCount+=1
        if(nums[i]==2): twoLastCount+=1

    for i in range(0,zerosLastCount):
        nums[i]=0

    for i in range(zerosLastCount,zerosLastCount+onesLastCount):
        nums[i]=1

    for i in range(zerosLastCount+onesLastCount,zerosLastCount+onesLastCount+twoLastCount):
        nums[i]=2

    return nums