def divide(dividend, divisor):

    flag = 1
    if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
        if(dividend<0 and divisor<0):
            dividend = -dividend
            divisor = - divisor
        flag=1
    else:
        if dividend<0 and divisor>0:
            dividend = -dividend
            flag=-1
        elif divisor<0 and dividend>0:
            divisor = -divisor
            flag=-1


    if (divisor > dividend):
        return 0
    if ((divisor + divisor) > dividend):
        if flag == -1: return -1
        return 1
    if ((divisor + divisor) == dividend):
        if flag==-1:return -2
        return 2

    sum = divisor
    totalState = 0
    while(True):
        previous, ans, next, state = 1, 0, 1, 0
        while(True):
            next = divisor<<state
            if next>=dividend-sum:
                break
            else:
                previous=next
                state+=1
        sum = sum+previous
        totalState = totalState+2**(state-1)
        if(sum+divisor>dividend):
            totalState+=1
            break
        if(sum+divisor==dividend):
            totalState += 2
            break


    if(totalState>=2147483648 and flag==1):
        totalState = 2147483647
    if flag == -1:
        return -totalState
    return totalState

print(divide(-1,1))
print(divide(-1,-1))
print(divide(-2147483648,1))