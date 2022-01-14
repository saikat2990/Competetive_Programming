def setZeroes(matrix):
    rows=[]
    cols=[]
    m = len(matrix)
    n = len(matrix[0])

    for i in range(0,m):
        for j in range(0,n):
            if(matrix[i][j]==0):
                rows.append(i)
                cols.append(j)
    for i in range(0,m):
        for j in range(0,n):
            if i in rows:
                matrix[i][j]=0
            if j in cols:
                matrix[i][j]=0

    print(matrix)
    return matrix


setZeroes([[1,1,1],[1,0,1],[1,1,1]])