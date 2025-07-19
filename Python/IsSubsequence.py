def isSubsequence(s,t):                 # Leetcode : 392
    pos = 0                             # Variable to iterate the s string

    for i in t:                         # Loop to go through string t.        
        if pos<len(s):                  # allow the loop to progress only if pos is less than len(s)
            if i == s[pos]:             # if the charaters in both string matches increment pos to 1
                pos += 1
    return pos == len(s)                # return if pos == len(s) : True or False

print(isSubsequence('abe','ahbgdc'))