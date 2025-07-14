def evalRPN(tokens):
    int_stack = []
    for i in tokens:
        if i.isdigit():
            int_stack.append(int(i))
        elif i[0] == '-' and len(i) > 1:
            int_stack.append(int(i))
        else:
            b = int_stack.pop()
            a = int_stack.pop()
            if i == '+':
                int_stack.append(int(a+b))
            elif i == '-':
                int_stack.append(int(a-b))
            elif i == '*':
                int_stack.append(int(a*b))
            elif i == '/':
                int_stack.append(int(a/b))
    return int_stack[-1]

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["4","3","-"]))