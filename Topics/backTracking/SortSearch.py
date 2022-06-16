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
            left = mid

        elif nums[mid]> nums[right]:
            right=right-1
            left = mid

        elif nums[right]>nums[mid] and target< nums[right] and target>nums[mid]:
            left = mid

        elif nums[right]>nums[mid] and target>nums[mid] and target> nums[right]:
            right = mid
        elif nums[mid]<nums[left]:
            left=left+1
            right = mid

        if (mid==0):
            return -1

        if left+1==right or right-1==left:
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            else: return -1


print(search([4,5,6,7,0,1,2],0))
print(search([1,3,5],0))