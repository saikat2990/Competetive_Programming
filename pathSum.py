
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = TreeNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = TreeNode(val)


class Solution:
    def printTree(self,currentNode,ans):
        if(currentNode==None):
            return
        if currentNode.right==None:
            ans.append("null")
        else: ans.append(currentNode.right.val)
        if currentNode.left==None:
            ans.append("null")
        else: ans.append(currentNode.left.val)
        self.printTree(currentNode.right, ans)
        self.printTree(currentNode.left,ans)

    def recursiveData(self,currentNode,target,currentList,ansList):
        if currentNode==None:
            return
        currentList.append(currentNode.val)
        if(currentNode.right==None and currentNode.left==None):
            if(sum(currentList)==target):
                ansList.append(list(currentList))
                print(currentList)
            if len(currentList) > 0:
                currentList.pop()
            return
        self.recursiveData(currentNode.right,target,currentList,ansList)
        self.recursiveData(currentNode.left, target, currentList, ansList)
        if len(currentList)>0:
            currentList.pop()


    def pathSum(self,root, targetSum: int):
        ansList=[]
        self.recursiveData(root,targetSum,[],ansList)
        print(ansList)
        return ansList

nums = [6,10,11,9,7,5,4,3,1]
bst = TreeNode(val=8,right=None,left=None)
for num in nums:
    bst.insert(num)
ans=[]
Solution().printTree(bst,ans)
print(ans)
Solution().pathSum(bst,27)