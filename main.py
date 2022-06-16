import copy


def recursiveExpressionAddOperator(num,iterator,totalIteratorList,target,currentNumberString,currentValue,value,actualAns):
    value.append(currentValue)
    totalIteratorList.append(currentNumberString)
    if (currentValue == target):
        actualAns.append(currentNumberString)
    if(iterator==(len(num))):
        return

    currentNumberString+=('*'+num[iterator])
    recursiveExpressionAddOperator(num,iterator+1,totalIteratorList,target,copy.deepcopy(currentNumberString),copy.deepcopy(currentValue*int(num[iterator])),value,actualAns)
    currentNumberString = currentNumberString.replace('*' + num[iterator],"")
    currentNumberString+=('+'+num[iterator])
    recursiveExpressionAddOperator(num,iterator+1,totalIteratorList,target,copy.deepcopy(currentNumberString),copy.deepcopy(currentValue+int(num[iterator])),value,actualAns)
    currentNumberString = currentNumberString.replace('+' + num[iterator],"")
    currentNumberString += ('-' + num[iterator])
    recursiveExpressionAddOperator(num, iterator + 1, totalIteratorList, target, copy.deepcopy(currentNumberString),
                                   copy.deepcopy(currentValue - int(num[iterator])),value,actualAns)
    currentNumberString = currentNumberString.replace('-' + num[iterator],"")


def addOperators(num, target):
    ans=[]
    value=[]
    actualAns=[]
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            currentValue = int(num[i])
            currentString = num[i]
            recursiveExpressionAddOperator(num,j,ans,target,currentString,currentValue,value,actualAns)
    print(ans)
    print(value)
    print(actualAns)

addOperators("232",8)