def groupAnagrams(strs):
    lst=[]
    tempLst=[]
    for eachWord in strs:
        eachWordTemp = sorted(eachWord)
        eachWordTemp = ''.join(eachWordTemp)
        flag=True
        if len(lst)==0:
            lst.append([eachWord])
            tempLst.append([eachWordTemp])
        else:
            for i in range(0,len(tempLst)):

                if eachWordTemp in tempLst[i]:
                    tempLst[i].append(eachWordTemp)
                    lst[i].append(eachWord)
                    flag = False
                    continue
                if eachWordTemp not in tempLst[i]:
                    if flag!=False:
                        flag = True

            if flag ==True:
                tempLst.append([eachWordTemp])
                lst.append([eachWord])

    print(lst)
    return lst


groupAnagrams(["a"])
# def stringPermutation(stringList):
#     if len(stringList)==0:
#         return []
#     if len(stringList)==1:
#         return [stringList]
#     lst =[]
#     for i in range(0,len(stringList)):
#         current = [stringList[i]]
#         rmlst = stringList[:i]+ stringList[i+1:]
#         for p in stringPermutation(rmlst):
#             lst.append(current+p)
#     return lst
#
# str = "12345"
# strList = list(str)
# print(len(strList))
# listofStr = []
# for p in stringPermutation(strList):
#     listofStr.append(p)
# print(len(listofStr))
# print(listofStr)