import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,node,currentList,ansList):
        if(node.left==None and node.right==None):
            currentList.append(node.val)
            print(currentList)
            data = list(map(str, currentList))
            ansList.append("->".join(data))
            return
        currentList.append(node.val)
        if node.left!=None:
            self.dfs(node.left,copy.deepcopy(currentList),ansList)
        if node.right!=None:
            self.dfs(node.right,copy.deepcopy(currentList),ansList)

    def binaryTreePaths(self, root):
        anslist=[]
        self.dfs(root,[],anslist)
        print(anslist)
        return anslist