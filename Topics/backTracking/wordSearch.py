def createString(board, rowIndex, colIndex, currentString, word, currentIndex, direction, exploreList):
    if len(currentString) == len(word):
        if currentString == word:
            return True
        else:
            return False

    if (rowIndex + 1) < len(board) and direction != "up":
        temp = currentString + board[rowIndex + 1][colIndex]
        if exploreList[rowIndex + 1][colIndex]==False and word[currentIndex+1]==board[rowIndex + 1][colIndex]:
            exploreList[rowIndex + 1][colIndex] = True
            if (createString(board, rowIndex + 1, colIndex, temp, word, currentIndex + 1, "down",
                             exploreList)):return True
            else:
                exploreList[rowIndex + 1][colIndex] = False

    if (rowIndex - 1) >= 0 and direction != "down":
        temp = currentString + board[rowIndex - 1][colIndex]
        if exploreList[rowIndex - 1][colIndex]==False and word[currentIndex+1]==board[rowIndex - 1][colIndex]:
            exploreList[rowIndex - 1][colIndex] = True
            if (createString(board, rowIndex - 1, colIndex, temp, word, currentIndex + 1, "up",
                             exploreList)): return True
            else:
                exploreList[rowIndex - 1][colIndex] = False

    if (colIndex + 1) < len(board[0]) and direction != "left":
        temp = currentString + board[rowIndex][colIndex + 1]
        if exploreList[rowIndex][colIndex+1]==False  and word[currentIndex+1]==board[rowIndex][colIndex + 1]:
            exploreList[rowIndex][colIndex+1] =True
            if (createString(board, rowIndex, colIndex + 1, temp, word, currentIndex + 1, "right",
                             exploreList)): return True
            else:
                exploreList[rowIndex][colIndex + 1] = False

    if (colIndex - 1) >= 0 and direction != "right":
        temp = currentString + board[rowIndex][colIndex - 1]
        if exploreList[rowIndex][colIndex-1] == False  and word[currentIndex+1]==board[rowIndex][colIndex - 1]:
            exploreList[rowIndex][colIndex-1] = True
            if (createString(board, rowIndex, colIndex - 1, temp, word, currentIndex + 1, "left",
                             exploreList)): return True
            else:
                exploreList[rowIndex][colIndex - 1] = False



def exist(board, word):
    row = len(board)
    col = len(board[0])
    isFound = False
    for i in range(0, row):
        for j in range(0, col):
            if word[0] == board[i][j]:
                x = [[False for i in range(10)] for j in range(10)]
                x[i][j]=True
                isFound = createString(board, i, j, board[i][j], word, 0, "", x)
                if isFound:
                    break
        if isFound:
            break
    if isFound == None:
        isFound = False
    print(isFound)
    return isFound


exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
exist([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]], "aaaaaaaaaaaaa")
exist([["a", "a", "b", "a", "a", "b"], ["a", "a", "b", "b", "b", "a"], ["a", "a", "a", "a", "b", "a"],
       ["b", "a", "b", "b", "a", "b"], ["a", "b", "b", "a", "b", "a"], ["b", "a", "a", "a", "a", "b"]], "bbbaabbbbbab")
exist([["a","b"],["c","d"]],"cdba")
exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]],"AAAAAAAAAAAAABB")
