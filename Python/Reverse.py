def reverse(x):                             # Leetcode : 7
    sign = -1 if x<0 else 1                 # extract the sign of input
    rev = 0                             
    x = abs(x)                              # make the input positive
    while x != 0:                       
        t = x % 10                          # pull the last digit out of the input
        x //= 10                            # remove the last digit from the input
        if rev > ((2**31) -1 -t) // 10:     # check if the num is in range -2^31 to 2^31 
            return 0                        # This condition has been simplified from this inequality:
        rev = rev * 10 + t                  # rev * 10 + digit <= 2**31 - 1
    return sign*rev                         # finally return the reversed number
print(reverse(-123))