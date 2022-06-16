class Solution(object):
    def createRecursiveList(self, stringList, str, n, leftOne, rightOne):

        if (leftOne < n):
            str += "("
            self.createRecursiveList(stringList, str, n, leftOne + 1, rightOne)
            str = str[:-1]
        if (rightOne < n and leftOne > rightOne):
            str = str + ")"
            self.createRecursiveList(stringList, str, n, leftOne, rightOne + 1)
            str = str[:-1]

        if (leftOne == n and rightOne == n):
            stringList.append(str)

    def generateParenthesis(self, n):
        stringList = []
        str = ""
        self.createRecursiveList(stringList, str, n, 0, 0)
        return stringList

