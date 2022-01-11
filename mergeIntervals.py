def merge(intervals:[]):
    b = sorted(intervals, key=lambda a:a[0])
    ans=[]
    ans.append(b[0])
    print(b)
    for index in range(len(b)):
        print(ans)
        if index!=0:
            if ans[len(ans)-1][1]>=b[index][0]:
                if ans[len(ans)-1][1]<b[index][1]:
                    data = ans.pop()
                    ans.append([data[0],b[index][1]])

            else:
                ans.append(b[index])

    print(ans)





merge([[2,3],[4,5],[6,7],[8,9],[1,10]])