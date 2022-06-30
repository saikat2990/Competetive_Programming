def addOperators(num, target):
    res=[]


def recursivelyAdd(num,temp,cur,last,res,target):
    if(not num):
        if cur==target:
            res.append(temp)
    for i in range(1,len(num)):
        val = num[:i]
        if(i==1 or (i>1 and num[0]!="0")):
            recursivelyAdd(num[i:],temp+"+"+val,cur+int(val),int(val),res,target)
            recursivelyAdd(num[i:],temp+"-"+val,cur-int(val),-int(val),res,target)
            recursivelyAdd(num[i:],temp+"*"+val,cur-last+last*int(val),int(val),res,target)



addOperators("123",5)