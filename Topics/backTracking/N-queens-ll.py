def solveNQueens(n):
    def backtrack(i):
        if i == n:
            res.append(list(board))
        for j in range(n):
            print("Before if: ",cols, diag, off_diag,i,j)
            if j not in cols and j - i not in diag and j + i not in off_diag:
                cols.add(j)
                diag.add(j - i)
                off_diag.add(j + i)
                print(cols,diag,off_diag)
                board.append("." * (j) + "Q" + "." * (n - j - 1))
                backtrack(i + 1)
                board.pop()
                off_diag.remove(j + i)
                diag.remove(j - i)
                cols.remove(j)

    res = []
    board = []
    cols = set()
    diag = set()
    off_diag = set()
    backtrack(0)
    return len(res)

print(solveNQueens(4))