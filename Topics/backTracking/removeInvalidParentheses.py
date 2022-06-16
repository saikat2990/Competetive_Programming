def removeInvalidParentheses(s):
    left=0
    right=0
    for char in s:
        if char=='(':
            left+=1
        elif char==')':
            right+=1
    print(left,right)
    if left>right:
        left = left-right
        right=0
    elif right>left:
        right=right-left
        left=0
    else:
        right=0
        left=0
    print(left, right)
removeInvalidParentheses("()())()")