def spiralOrder(number):
    matrix  = [[0 for i in range(number)] for j in range(number)]
    right=len(matrix)-1
    down=len(matrix)-1
    left=0
    up=1
    ans=[]
    row=0
    col=-1
    count=1
    while(1):
        for i in range(left,right+1):
            col+=1
            matrix[row][i]=count
            count+=1
        if count > number * number: break

        right-=1


        for j in range(up,down+1):
            row+=1
            matrix[j][col] = count
            count += 1
        down-=1
        if count > number * number: break

        for k in range(right,left-1,-1):
            col-=1
            matrix[row][k]= count
            count += 1

        left+=1

        if count > number * number: break
        for l in range(down,up-1,-1):
            row-=1
            matrix[l][col]= count
            count += 1
        up+=1
        if count > number * number: break

    return(matrix)
print(spiralOrder(1))