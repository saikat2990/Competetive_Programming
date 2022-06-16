# import copy
#
#
# def getAllPossibleList(board, currentString, rowLen, colLen, r, c, char, resultList, indexList):
#     currentString += char
#     print(currentString, r, c, rowLen, colLen, indexList)
#     if r < 0 or r == rowLen or c == colLen or c < 0:
#         return
#     if c + 1 < colLen:
#         item = str(r) + str(c + 1)
#         if item not in indexList:
#             indexList.append(item)
#             getAllPossibleList(board, currentString, rowLen, colLen, r, c + 1, board[r][c + 1], resultList, indexList)
#             currentString = currentString[:-1]
#             indexList = indexList[:-1]
#     if r + 1 < rowLen:
#         item = str(r + 1) + str(c)
#         if item not in indexList:
#             indexList.append(item)
#             getAllPossibleList(board, currentString, rowLen, colLen, r + 1, c, board[r + 1][c], resultList, indexList)
#
#     if c - 1 >= 0:
#         item = str(r) + str(c - 1)
#         if item not in indexList:
#             indexList.append(item)
#             getAllPossibleList(board, currentString, rowLen, colLen, r, c - 1, board[r][c - 1], resultList, indexList)
#
#     if r - 1 >= 0:
#         item = str(r - 1) + str(c)
#         if item not in indexList:
#             indexList.append(item)
#             getAllPossibleList(board, currentString, rowLen, colLen, r - 1, c, board[r - 1][c], resultList, indexList)
#     return
#
#
# def findWords(board, words):
#     row = len(board)
#     col = len(board[0])
#     result = []
#     getAllPossibleList(board, "", row, col, 0, 0, board[0][0], result, [])
#     # for i in range(0,row):
#     #     for j in range(0,col):
#
#
# findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
#           ["oath", "pea", "eat", "rain"])
import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False

class NodeCredential:
    def __init__(self):
        self.root = Node()

    def insertNode(self,Word):
        node = self.root
        for w in Word:
            node = node.children[w]
        node.isWord = True

class Solution:
    def dfs(self,board,r,c,node,res,currentString):
        if node.isWord and currentString not in res:
            res.append(currentString)
        if r<0 or r==len(board) or c<0 or c==len(board[0]):
            return
        temp = board[r][c]
        node = node.children.get(temp)
        if not node:
            return
        board[r][c]='#'
        self.dfs(board,r+1,c,node,res,currentString+temp)
        self.dfs(board,r,c+1,node,res,currentString+temp)
        self.dfs(board,r-1,c,node,res,currentString+temp)
        self.dfs(board,r,c-1,node,res,currentString+temp)
        board[r][c] = temp

    def findWords(self, board, words):
        nodePa = NodeCredential()
        node = nodePa.root
        res=[]
        for word in words:
            nodePa.insertNode(word)

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                self.dfs(board,i,j,node,res,"")
        print(res)
        return res


Solution().findWords( [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])