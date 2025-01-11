def balanced_parenthesis(str):
    stack=[]
    dic_str={')':'(','}':'{',']':'['}
    for char in str:
        if char in dic_str:
           if stack and stack[-1]==dic_str[char]:
                stack.pop()
           else:
               return False
        else:
            stack.append(char)
    return not stack
print(balanced_parenthesis("({[]})"))