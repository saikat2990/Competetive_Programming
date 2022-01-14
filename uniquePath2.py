def uniquePaths(obstacleGrid ):
    if(obstacleGrid[0][0]==1):return 0
    m=len(obstacleGrid )
    n=len(obstacleGrid[0])
    print(m,n)
    matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(0,m):
        for j in range(0,n):
            if(i==0 or j==0):
                if(obstacleGrid[i][j]!=1):
                    if(i==0 and j!=0 and obstacleGrid[i][j-1]!=1 and matrix[i][j-1]!=0):matrix[i][j]=1
                    if (j == 0 and i != 0 and obstacleGrid[i-1][j] != 1and matrix[i-1][j]!=0): matrix[i][j] = 1
                    if(i==0 and j==0 ):matrix[i][j]=1
            elif(obstacleGrid[i][j]!=1):
                if((matrix[i - 1][j] + matrix[i][j - 1])!=0):matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]


    return matrix[m-1][n-1]


print(uniquePaths([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))