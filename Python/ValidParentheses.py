# My method
def validParentheses1(s):                                        # Leetcode : 20
    stack = []                                                  # create a stack list
    for i in s:                                                 # traverse the string s
        if i in {'(','[','{'}:                                  # if i belongs to open braces
            stack.append(i)                                     # push to the list
        else:                                       
            if stack:                                           # else check if stack has a element
                if i == ')' and stack[len(stack)-1] == '(':     # if so check which closing bracket
                    stack.pop()                                 # only if the brackets match pop the last element from stack
                elif i == ']' and stack[len(stack)-1] == '[':   # continue this step for both the brackets
                    stack.pop()
                elif i == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                else:                                           # if the pairs doesn't match return False
                    return False
            else:                                               # if there's no element in stack return False
                return False                                    # because the first element is a closing bracket
    return stack == []                                          # finally check if there is any remaining brackets left in the stack.

# compressed method
def validParentheses2(s):                       # Leetcode : 20
    pair = {')':'(',']':'[','}':'{'}            # create a dictionary to have the brackets as key:value pairs
    stack = []                                  # create a stack
    for i in s:                                 # use loop to traverse the string
        if i in pair.values():                  # check if i is a opening bracket
            stack.append(i)                     # if so push the value to the stack
        elif stack and stack[-1] == pair[i]:    # elif if there is a element in stack and the last term is a pair of i
            stack.pop()                         # pop the element from the stack
        else:
            return False                        # else return False
    return stack == []                          # finally check if there any element remaining in the stack

print(validParentheses2("()[]{}{"))