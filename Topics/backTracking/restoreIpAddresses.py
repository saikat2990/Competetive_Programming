import copy
def isValid(subIp):
    if len(subIp) == 0:
        return False
    if subIp[0]=='0' and len(subIp)>1:
        return False
    if len(subIp)>3 or int(subIp)>255:
        return False

    return True

def backtracking(ip,currentString,currentList:[],ansList:[],start):
    #print(currentList,currentString)
    if isValid(currentString):
        currentList.append(currentString)
        if(len(currentList)==4):
            if len(''.join(currentList))==len(ip):
                ansList.append(list(currentList))
            currentList=[]
        currentString=''
    else:
        if len(currentList)==3:
            currentList=[]
            return
    for i in range(start,len(ip)):
        currentString+=ip[i]
        backtracking(ip,copy.deepcopy(currentString),currentList.copy(),ansList,i+1)
        #print(currentList,currentString,"After")

def restoreIpAddresses(ip):
    ansList=[]
    backtracking(ip,"",[],ansList,0)
    actualAnsList=[]
    for item in ansList:
        actualAnsList.append('.'.join(item))
    return actualAnsList


restoreIpAddresses("25525511135")
restoreIpAddresses("0000")
restoreIpAddresses("101023")