def uniquePaths(grid):
    m=len(grid )
    n=len(grid[0])

    matrix = [[0 for i in range(n)] for j in range(m)]
    matrix[0][0] = grid[0][0]
    for i in range(0,m):
        for j in range(0,n):
            if (i==0 and j==0):continue
            if(i==0 and j>0):
                matrix[i][j]=grid[i][j]+matrix[i][j-1]
            elif(j==0 and i>0):
                matrix[i][j]=grid[i][j]+matrix[i-1][j]
            else:
                if((matrix[i - 1][j] +grid[i][j]) >(matrix[i][j - 1]+grid[i][j])):
                    matrix[i][j] =matrix[i][j - 1]+grid[i][j]
                else:
                    matrix[i][j] =matrix[i - 1][j] +grid[i][j]


    return matrix[m-1][n-1]


print(uniquePaths([[1]]))