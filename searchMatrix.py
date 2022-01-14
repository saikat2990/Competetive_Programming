def searchMatrix(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    if(matrix[0][0]>target or matrix[row-1][col-1]<target):
        return False
    for i in range(0,row):
        if(matrix[i][0]<= target and matrix[i][col-1]>=target):
            for j in range(0,col):
                    first = 0
                    last = len(matrix[i]) - 1
                    while (first <= last):
                        mid = (first + last) // 2
                        if matrix[i][mid] == target:
                            return True
                        elif target < matrix[i][mid]:
                            last = mid - 1
                        else:
                            first = mid + 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],1))