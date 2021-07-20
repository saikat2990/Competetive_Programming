def search(nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid = (left + right) // 2
        if (nums[mid] == target):
            return mid

        elif left == mid == right:
            return -1
        elif nums[left]==target:
            return left
        elif nums[right]==target:
            return right
        elif nums[left] < nums[mid] and target<nums[mid] and target>nums[left] :
           right=mid

        elif nums[left] < nums[mid] and target < nums[mid] and target < nums[left]:
            if nums[left]<nums[right]:
                return -1
            left = mid

        elif nums[mid]> nums[right]:
            right=right-1
            left = mid

        elif nums[right]>nums[mid] and target< nums[right] and target>nums[mid]:
            left = mid

        elif nums[right]>nums[mid] and target>nums[mid] and target> nums[right]:
            if nums[right]>nums[left]:
                return -1
            right = mid
        elif nums[mid]<nums[left]:
            left=left+1
            right = mid

        print(left,right,mid)
        if (mid==0):
            return -1

        if left+1==right or right-1==left:
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            else: return -1

def searchRange(nums, target):
    array =[]
    firstIndex = search(nums, target)
    array.append(firstIndex)
    print(firstIndex)
    deletedIndex=[]
    if firstIndex != -1 and len(nums) > 0:
        deletedIndex.append(firstIndex)
        del nums[firstIndex]
    increment=1
    if firstIndex!=-1:
        while search(nums,target)!=-1:
            if deletedIndex[0]<= search(nums,target):
                array.append(search(nums, target)+increment)
            else:
                array.append(search(nums, target))
            firstIndex = search(nums, target)
            print(firstIndex)
            if firstIndex!=-1 and len(nums)>0:
                deletedIndex.append(firstIndex)
                deletedIndex.sort()
                del nums[firstIndex]

                increment += 1
            else: break
            print(deletedIndex, array, nums)
            print(search(nums,target))
    if len(array)==1:
        array.append(firstIndex)
    array.sort()
    if len(array)==1:  array.append(-1)
    print(array)
    ans=[]
    ans.append(array[0])
    ans.append(array[len(array)-1])
    return ans
#
# # print(searchRange([5,7,7,8,8,10],8))
# # print(searchRange([1,1,2],1))
# # print(searchRange([5,7,7,8,8,10],6))
# # print(searchRange([3,3,3,3,3,3],3))
# # print(searchRange([1],1))
# # print(searchRange([1,2,2],2))
# # print(searchRange([1,2,3,3,3,3,4,5,9],3))
# print(searchRange([0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11],0))



print(search([4,5,6,7,0,1,2],0))
print(search([1,3,6,5],0))
print(search([1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11],0))
print(search([0,0,0,0,0,1,2,2,3,4,4,4,4,5,5,5,6],0))
print(searchRange([0,0,0,0,0,1,2,2,3,4,4,4,4,5,5,5,6],5))
