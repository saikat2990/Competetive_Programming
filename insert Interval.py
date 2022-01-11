def insert(intervals, newInterval):

    if(len(intervals)==0):
        return [newInterval]
    if(len(intervals)==1):
        if intervals[0][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        if newInterval[1]<intervals[0][0]:
            ans=[]
            ans.append(newInterval)
            ans.append(intervals[0])
            return ans
        ans=[intervals[0][0],intervals[0][1],newInterval[0],newInterval[1]]
        ans.sort()
        return [[ans[0],ans[3]]]
    firstElementFound=False
    intervalFirstElement = -1
    ans=[]
    if(newInterval[0]>intervals[len(intervals)-1][1]):
        intervals.append(newInterval)
        return intervals
    if (newInterval[0] < intervals[0][0]):
        firstElementFound=True
        intervalFirstElement = newInterval[0]
        if(intervals[len(intervals)-1][1]<newInterval[1]):
            return [newInterval]
        if(intervals[0][0]>newInterval[1]):
            ans=[]
            ans.append(newInterval)
            ans.extend(intervals)
            return ans
    for (index,element) in enumerate(intervals):
        if(firstElementFound==False and intervalFirstElement == -1 and element[0]>newInterval[1]):
            ans.append(newInterval)
            for i in range(index,len(intervals)):
                ans.append(intervals[i])
            break
        elif(firstElementFound==False and intervalFirstElement == -1 and element[1]>=newInterval[0]):
            if(element[0]<newInterval[0]):
                intervalFirstElement = element[0]
            else: intervalFirstElement=newInterval[0]
            firstElementFound=True

            if(index==len(intervals)-1 and newInterval[0]<element[0]):
                temp = [element[0], element[1], newInterval[0], newInterval[1]]
                temp.sort()
                ans.append([temp[0], temp[3]])
                return ans
            if(newInterval[1]<=element[1]):
                firstElementFound=False
                ans.append([intervalFirstElement,element[1]])
        elif (firstElementFound == True and element[0] > newInterval[1]):
            firstElementFound = False
            ans.append([intervalFirstElement, newInterval[1]])
            ans.append(element)
        elif (firstElementFound == True and element[1] >= newInterval[1]):
            firstElementFound = False
            ans.append([intervalFirstElement, element[1]])
        elif(firstElementFound == False):
            ans.append(element)

    if(firstElementFound):
        ans.append([intervalFirstElement,newInterval[1]])
    return ans

print(insert([[3,6],[9,9],[11,13],[14,14],[16,19],[20,22],[23,25],[30,34],[41,43],[45,49]],[29,32]))