def isHappy(n):                                         # Leetcode : 202
    seen = set()                                        # create a set to note down the seen numbers to avoid infinite loop
    while n!=1 and n not in seen:                       # use the condition that n shouldn't be equal to 1 and n should not be inside seen.
        seen.add(n)                                     # add n to seen
        n = sum(int(digit)**2 for digit in str(n))      # add the square of digits in n 
    return n == 1                                       # return if n==1 or not
print(isHappy(2))