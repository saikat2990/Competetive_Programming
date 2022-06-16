def wordBreak(s,wordDict):
    res = []
    dfs(s, [], res,wordDict)
    return res

def isPal(path,wordDict):
    for i in range(0,len(path)):
        if path[i] not in wordDict:
            return False
    return True
def dfs(s, path, res,wordDict):
    if len(s)==0:
        #print(s, path)
        if isPal(path,wordDict):
            print(path)
            res.append(" ".join(path))
        return
    for i in range(1,len(s)+1):
        dfs(s[i:],path+[s[:i]],res,wordDict)




print(wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))