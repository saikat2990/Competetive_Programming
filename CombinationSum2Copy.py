class Solution:
    def combinationSum2(self, candidates, target):
        self.output = list()
        self.backtrack(target,list(),0,sorted(candidates))
        return self.output
    def backtrack(self,remain,curr,start,cands):
        if remain  == 0:self.output.append(list(curr))
        for i in range(start,len(cands)):
            if cands[i] > remain:
                break
            if i != start and cands[i] == cands[i-1]:
                continue
            curr.append(cands[i])
            self.backtrack(remain-cands[i],curr,i+1,cands)
            curr.pop()