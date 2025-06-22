def isPalindrome(s):                                           # Leetcode : 125
    s = (''.join(c for c in s if c.isalnum())).lower()         # extract only the alpha and num from s and make it lowercase
    return s == s[::-1]                                        # returns true if it's a palindrome
print(isPalindrome("0P"))