def listAddRecursively(firstIndex,secondIntex,nums,currentArr,currentTotal,ansList,iteration):
    if firstIndex+currentTotal<=len(nums) and iteration<len(nums):
        if len(currentArr)==currentTotal and iteration==len(nums)-1:
            ansList.append(currentArr)
            if secondIntex+(currentTotal-2)<len(nums)-1:
                listAddRecursively(firstIndex,secondIntex+1,nums,[nums[firstIndex]],currentTotal,ansList,secondIntex+1)
            else:
                first = firstIndex+1
                listAddRecursively(first, first + 1, nums, [nums[first]], currentTotal, ansList,
                                          first + 1)
        elif len(currentArr)==currentTotal and iteration!=len(nums)-1:
            ansList.append(currentArr)
            listAddRecursively(firstIndex, secondIntex + 1, nums, currentArr[:len(currentArr)-1], currentTotal, ansList, iteration)

        else :
            currentArr.append(nums[iteration])
            listAddRecursively(firstIndex, secondIntex, nums, currentArr, currentTotal, ansList, iteration + 1)
    else:
        return ansList

def subsets(nums):
    for i in range(2,len(nums)):
        result = listAddRecursively(0, 1, nums, [nums[0]], i, [], 1)
        print(result)


subsets([1,2,3,4,5,6,7,8])