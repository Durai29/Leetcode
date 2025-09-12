def isUgly(n):                  # Leetcode : 263
    if n == 0: return False     # return false if n = 0
    while n % 2 == 0: n//=2     # remove all the 2's from n
    while n % 3 == 0: n//=3     # remove all 3's from n
    while n % 5 == 0: n//=5     # remove all 5's from n
    return n == 1               # return true if n==1
