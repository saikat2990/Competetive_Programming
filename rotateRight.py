def rotateRight(path):
    # dotFound=0
    # backSlashFound=0
    # ans=""
    # parentFound=0
    #
    # for i in range(0,len(path)):
    #     if(path[i]=="/"):
    #         backSlashFound+=1
    #         dotFound=0
    #         if(parentFound>0):
    #             parentFound-=1
    #         continue
    #
    #     if(path[i]=="."):
    #         dotFound+=1
    #         if(i+2==len(path) and dotFound>2):
    #             ans +=(dotFound * ".")
    #         continue
    #
    #     if (dotFound > 2):
    #         ans += "/"+(dotFound * ".")
    #
    #     if (backSlashFound > 0 and len(ans)>0):
    #         if(ans[len(ans)-1]!="/"):
    #             ans += '/'
    #
    #     if(dotFound==2 and len(ans)>1):
    #         parentFound=1
    #
    #     if(dotFound==1 and backSlashFound==0):
    #         ans+='.'
    #
    #     if(parentFound==0):
    #         ans+=path[i]
    #
    #     dotFound=0
    #     backSlashFound=0
    #
    # ans="/"+ans
    # print(ans)
    ans=""
    temp=""
    backSlashFound=0
    removelist=[]
    for i in range(0,len(path)):
        if(path[i]=='/'):
            backSlashFound+=1
            continue
        if(backSlashFound>0):
            temp+="/"
            backSlashFound=0
        temp+=path[i]

    ansList = temp.split("/")

    for i in range(0,len(ansList)):
        if(ansList[i]==".."):
            removelist.append(i)
            addValue=i-1
            while(True):
                if addValue in removelist:
                    addValue-=1
                    continue
                else:
                    removelist.append(addValue)
                    break
        if(ansList[i]=="."):
            removelist.append(i)

    for i in range(0,len(ansList)):
        if i not in removelist:
            if(ansList[i]):
                ans+="/"+ansList[i]
    if(ans==""):
        ans="/"
    print(ans)
    return ans


rotateRight('/../C:/projects/workspace/testing/../testing/./file1.txt/')
rotateRight('/home/')
rotateRight('/../')
rotateRight('/home//foo/')
rotateRight('/a/./b/../../c/')
rotateRight("///a/b/../.././b/")