import copy


def recursiveExpressionAddOperator(num,iterator,totalIteratorList,target,currentNumberString,currentValue,value,actualAns):
    value.append(currentValue)
    totalIteratorList.append(currentNumberString)
    if(iterator==(len(num)-1)):
        if (eval(currentNumberString+num[iterator]) == target):
            actualAns.append(currentNumberString+num[iterator])
        return
    recursiveExpressionAddOperator(num,iterator+1,totalIteratorList,target,currentNumberString+num[iterator]+'*',eval(currentNumberString+num[iterator]),value,actualAns)
    recursiveExpressionAddOperator(num,iterator+1,totalIteratorList,target,currentNumberString+num[iterator]+'+',eval(currentNumberString+num[iterator]),value,actualAns)
    recursiveExpressionAddOperator(num, iterator + 1, totalIteratorList, target, currentNumberString+num[iterator]+'-',eval(currentNumberString+num[iterator]),value,actualAns)
    if (currentNumberString and currentNumberString[-1] not in ["+","-","*"] and num[iterator]=="0") or num[iterator]!="0" :
        recursiveExpressionAddOperator(num, iterator + 1, totalIteratorList, target,
                                       currentNumberString + num[iterator],
                                       eval(currentNumberString + num[iterator]), value, actualAns)

def addOperators(num, target):
    ans=[]
    value=[]
    actualAns=[]
    recursiveExpressionAddOperator(num,0,ans,target,"",0,value,actualAns)
    print(ans)
    print(value)
    print(actualAns)
    return actualAns

addOperators("105",5)

#accepted

import copy

class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)