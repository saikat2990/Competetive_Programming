def calculatePow(totalValue,x,n):
    if n==0:
        return 1
    if n%2==0:
        totalValue = calculatePow(totalValue,x,n//2)**2
    elif n%2==1:
        totalValue = calculatePow(totalValue,x,n-1)*x
    return totalValue

def myPow(x, n):
    if n<0:
        x=1/x
        n=-n
    return (calculatePow(1,x,n))





print(myPow(3,3))
print(myPow(3,4))
print(myPow(2,10))
print(myPow(2.00,-2))