def search(nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid = (left + right) // 2
        if (nums[mid] == target):
            return mid

        elif left == mid == right:
            return -1

        elif nums[left] <= target and nums[mid]>target:
            if nums[left]==target:
                return left
            left+=1
        elif nums[mid]<target and nums[right]>=target:
            if nums[right]==target:
                return right
            right-=1




print(search([4,5,6,7,8,0,1,2,3],2))