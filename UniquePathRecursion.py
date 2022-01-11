def getpath(m, n, right, down, count):
    if(m-1==down and n-1==right):
        count += 1
        return count
    if(m-1>down):
        count=getpath(m,n,right,down+1,count)
    if(n-1>right):
        count=getpath(m, n, right + 1, down, count)
    return count

def uniquePaths(m,n):
    getTotalPath = getpath(m,n,0,0,0)
    print(getTotalPath)

uniquePaths(3,5)