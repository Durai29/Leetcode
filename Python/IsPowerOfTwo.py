def isPowerOfTwo(n):                                    # Leetcode : 231
    binary = bin(n)                                     # convert the integer to binary
    return binary[2]=='1' and binary.count('1')==1      # check if it starts with 1 and the count of 1 is 1

print(isPowerOfTwo(8))
print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(2))

# Method 2
def isPowerOfTwo_2(n):            # Leetcode : 231
        if n == 0 :             # edge condition for 0
            return False        # return false
        return n & (n-1) == 0   # else do a and bit operation to check with n 
												        # and n-1 should return 0

# Revised Today ( 15 AUG 2025 )