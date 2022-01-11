def spiralOrder(matrix: [[]]):
    right=len(matrix[0])-1
    down=len(matrix)-1
    left=0
    up=1
    ans=[]
    row=0
    col=-1
    while(1):
        if left>right:break
        for i in range(left,right+1):
            col+=1
            ans.append(matrix[row][i])


        right-=1

        if(up>down): break
        for j in range(up,down+1):
            row+=1
            ans.append(matrix[j][col])
        down-=1

        if left>right: break
        for k in range(right,left-1,-1):
            col-=1
            ans.append(matrix[row][k])

        left+=1

        if up>down: break
        for l in range(down,up-1,-1):
            row-=1
            ans.append(matrix[l][col])
        up+=1

    print(ans)



spiralOrder([[1,2,3,4,10,78],
             [5,6,7,8,9,87],
             [9,10,11,12,1,98],
             [98,100,911,-12,7,90],
             [98,100,911,-12,7,90]])