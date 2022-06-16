def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
def convert(nums):
    data=[]
    for i in range(0,len(nums)):
        data.append(nums[i])
    ans = []
    for p in permutation(data):
        ans.append(p)
    return ans
def permute(nums):
    convert(nums)

permute([1,-2,3])