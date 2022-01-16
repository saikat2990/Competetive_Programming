def calculate(nums:[],index,k,arr:[],ans:[]):
    if (len(arr) == k):
        if arr not in ans:
            ans.append(arr.copy())
        return ans
    if(index==len(nums)):
        return ans

    arr.append(nums[index])
    ans = calculate(nums,index+1,k,arr,ans)
    arr.pop()
    ans = calculate(nums, index + 1, k, arr, ans)
    return ans

def combine(n,k):
    nums=[]
    for i in range(1,n+1):
        nums.append(i)
    ans = []
    for i in range(0,n):
     ans = calculate(nums,i,k,[],ans)

    return ans


combine(1,1)