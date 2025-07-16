def carFleet(target,position,speed):                        # Leetcode : 853
    pair = [[p,s] for p, s in zip(position,speed)]          # merge both position and speed list into a single list
    stack = []                                              # create a stack
    for p , s in sorted(pair)[::-1]:                        # Sort the pair list in descending order to go from right to left
        stack.append((target-p)/s)                          # push the time the element reaches the target
        if len(stack) > 1 and stack[-1] <= stack[-2]:       # now if there is 2 elements in the stack and top is less than the element below
            stack.pop()                                     # pop it, coz at some time the element would collide with the slower one
    return len(stack)                                       # return the lenght of the stack

print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
print(carFleet([0,4,2],[2,1,3],10))