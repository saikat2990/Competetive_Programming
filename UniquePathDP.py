def uniquePaths(m: int, n: int):
    matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(0,m):
        for j in range(0,n):
            if(i==0 or j==0):
                matrix[i][j]=1
            else:
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]

    return matrix[m-1][n-1]


print(uniquePaths(5,5))