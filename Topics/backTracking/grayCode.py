

def grayCode(n):
    current = [i^(i>>1) for i in range(2**n)]
    print(current)


grayCode(3)
