def canJump(nums: []):
    steps=1
    element=nums[0]
    tag=False
    if(len(nums)==1 or element>=(len(nums)-1)):
        return True
    for index in range(1,len(nums)):
        if (nums[index]>(element-steps) and (element-steps)>=0):
            element=nums[index]
            steps=1
            print(index, nums[index], element, steps)
            if(nums[index]+index)>=(len(nums)-1):
                tag=True
                break
        else:
            steps+=1
    return tag

print(canJump([1,3]))