def evalRPN(tokens):                        # Leetcode : 150
    int_stack = []                          # create a stack
    for i in tokens:                        # use for loop to iterate the input
        if i.isdigit():                     # check if the element is a digit?
            int_stack.append(int(i))        # if so push to the stack
        elif i[0] == '-' and len(i) > 1:    # elif it's a negative integer push it to the stack again
            int_stack.append(int(i))
        else:                                   
            b = int_stack.pop()             # keep in mind that in stack FILO is used so, the first popped element would be 'B'
            a = int_stack.pop()             
            if i == '+':                    # if it's an operator then, pop last two elements and do the corresponding
                int_stack.append(int(a+b))  # operation associated with it.
            elif i == '-':                  # after the operation push the result to the stack again
                int_stack.append(int(a-b))  
            elif i == '*':
                int_stack.append(int(a*b))
            elif i == '/':
                int_stack.append(int(a/b))
    return int_stack[-1]            

# optimal method: 
def evalRPN(tokens):                        # Leetcode : 150 
        stack = []                          # create stack
        for token in tokens:                # use loop to traverse
            if token not in "+-*/":         # check if element not belongs to the operators
                stack.append(int(token))    # if so push to the stack
            else:                           
                b = stack.pop()             # else pop last 2 elements and do the corresponding operation
                a = stack.pop()             # push the result to the stack again
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Truncate toward zero
                    stack.append(int(a / b))
        return stack[0]                     # return the last element

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","","/","","17","+","5","+"]))
print(evalRPN(["4","3","-"]))

def evalRPN(tokens):
    stack = []
    for i in tokens:
        # if stack:
            if i not in {'+','-','/','*'}:
                stack.append(int(i))
            elif len(i) < 2:
                b = stack.pop()
                a = stack.pop()
                if i == '+': stack.append(a+b)
                elif i == '-': stack.append(a-b)
                elif i == '*': stack.append(a*b)
                elif i == '/': stack.append(int(a/b))

            else:
                stack.append(int(i))
        # else:
        #     stack.append(i)
    return stack[-1]

# same logic but small modification
# Revised ( 22 Jul 2025 ) 1
# Revised ( 01 Aug 2025 ) 2