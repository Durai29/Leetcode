class MinStack:                                                 # Leetcode : 155
    def __init__(self): 
        self.stack = []                                         # create a stack to store all elements inside this list
        self.min_stack = []                                     # create another stack to store only the minimum integer to this list

    def push(self,val):                                         # this method is used to push elements to the stacks
        if not self.min_stack or val <= self.min_stack[-1]:     # here push element to minstack only if it's empty 
            self.stack.append(val)                              # or element is lesser than existing one
            self.min_stack.append(val)                          
        else:                                                   # else push only to the main stack
            self.stack.append(val)

    def pop(self):                                              # remove elements from the list
        popped = self.stack.pop()                               # pop the element from the main stack
        if popped == self.min_stack[-1]:                        # if the popped element is equal to the minimum element in minstack
            self.min_stack.pop()                                # remove the element from minstack also

    def top(self):                                              # return the last element from the main stack
        return self.stack[-1]

    def getMin(self):                                           # return the last element from the minstack
        return self.min_stack[-1]

# Test cases:
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-1)
print(stack.getMin())
print(stack.top())
stack.pop()
print(stack.getMin())

# Revised today ( 26 JUL 2025 )
# Revised today ( 02 AUG 2025 )