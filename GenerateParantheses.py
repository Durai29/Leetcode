def generateParantheses(n):                                     # Leetcode : 22
    result = []                                                 # create a list to store the set of result
    def operate(current, openCount, closeCount):                # is method is used to recursively create the branches of the tree
        if len(current) == 2 * n:                               # this condition checks for the bracket limit
            result.append(current)                              # if reached append it to the result
            return                                              # return to break the branch
        
        if openCount < n:                                       # if opencount is less than n then 
            operate(current + '(' , openCount + 1, closeCount)  # add '(' to current and increment opencount
        
        if closeCount < openCount:                              # if closecount is less than opencount 
            operate(current + ')', openCount, closeCount + 1)   # add ')' to current and increment closecount
                                                                # this is the condition to check for valid parantheses
    operate('', 0, 0)                                           # call the function to start the recursion and make the tree

    return result                                               # return the result
        
print(generateParantheses(2))