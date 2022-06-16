
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursiveData(self,start,end):
        if start>end:
            return [None]
        ansNode=[]
        for i in range(start,end+1):
            lelfNodes= self.recursiveData(start,i-1)
            rightNodes = self.recursiveData(i+1,end)
            for l in lelfNodes:
                for r in rightNodes:
                    node = TreeNode(val=i,left=None,right=None)
                    node.right = r
                    node.left = l
                    ansNode.append(node)
        return ansNode

    def printTree(self,currentNode,ans):
        if(currentNode==None):
            return
        ans.append(currentNode.val)
        if currentNode.right==None:
            ans.append("null")
        self.printTree(currentNode.right,ans)
        if currentNode.left==None:
            ans.append("null")
        self.printTree(currentNode.left,ans)

    def generateTrees(self, n: int):
        allanswer =  self.recursiveData(1,n)
        for i in range(0,len(allanswer)):
            answer=[]
            self.printTree(allanswer[i],answer)
            print(answer)


Solution().generateTrees(3)