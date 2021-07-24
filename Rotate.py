def rotate(matrix):
    n = len(matrix)
    mid = n//2
    for i in range(0,mid):
        temp = matrix[i]
        matrix[i] = matrix[n-1-i]
        matrix[n-1-i] = temp
    for i in range(0,n):
        for j in range(0,i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))