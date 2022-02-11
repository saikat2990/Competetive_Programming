def getRecursiveAns(ansList,currentList,position,n):
    if(position+1==n):
        ansList.append(currentList)
        return
    for i in range(position,n):
        print(currentList)
        currentList[i]=0
        getRecursiveAns(ansList,currentList.copy(),position+1,n)
        currentList[i]=1
def grayCode(n):
    ansList=[]
    currentList = [0 for i in range(n)]
    getRecursiveAns(ansList,currentList.copy(),0,n)
    print(ansList)

grayCode(2)