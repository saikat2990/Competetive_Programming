class Solution(object):
    def hasMaximumValue(self,ansArray,cadidateElement):
        for i in range(0,len(ansArray)):
            if ansArray[i] > cadidateElement:
                return True
        return False

    def recursivelyCount(self,candidates,target,ansArray,totalArray):
        sumValue = sum(ansArray)
        if sumValue > target:
            return ansArray

        if sumValue == target:
            print(ansArray, "werwer")
            totalArray.append(ansArray)
            return ansArray

        for i in range(0,len(candidates)):
            if self.hasMaximumValue(ansArray,candidates[i])!=True:
                sumValue+=candidates[i]
                ansArray.append(candidates[i])
                ansArray = self.recursivelyCount(candidates,target,ansArray,totalArray)
                ansArray = ansArray[:len(ansArray)-1]
        return ansArray

    def combinationSum(self,candidates, target):
        totalArray=[]
        print(self.recursivelyCount(candidates,target,[],totalArray))
        return totalArray
