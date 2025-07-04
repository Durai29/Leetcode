def isPalindrome1(s):                                           # Leetcode : 125
    s = (''.join(c for c in s if c.isalnum())).lower()         # extract only the alpha and num from s and make it lowercase
    return s == s[::-1]                                        # returns true if it's a palindrome

def isPalindrome2(s):    # Leetcode : 125
    # s = ''.join([i for i in s.lower() if i.isalnum()])    # change the string to lowercase and only append alphabet or numbers to the list
    # return s == s[::-1]                                   # convert the list to string and return True if it's a palindrome
    

    l , r = 0 , len(s)-1                        # Two pointers
    while l < r:                                # while L is less than R ( Strictly )
        while l < r and not s[l].isalnum():     # use this loop to find a char which is alphabet or number from left
            l += 1
        while l < r and not s[r].isalnum():     # use this loop to find a char which is alphabet or number form right
            r -= 1
        if s[l].lower() != s[r].lower():        # check if both are not same
            return False                        # if so return False
        l += 1                                  # then increment both L and R
        r -= 1

    return True                                 # return True if the loop has executed successfully

print(isPalindrome2("0P"))