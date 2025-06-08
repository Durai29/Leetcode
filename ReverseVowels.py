def reverseVowels(s):                                           # Problem : 345
    s = list(s)                                                 # convert str to list
    left , right = 0, len(s)-1                                  # Here we're using 2 pointers 
    while left < right:                                         # condition to break the 2 pointers properly
        while left<right and s[left].lower() not in 'aeiou':    # The left<right condition is important because the 
            left += 1                                           # program will negate the process again to the start.
        while left<right and s[right].lower() not in 'aeiou':   # We would get the same answer If this condition is not 
            right -=1                                           # present.
        s[left],s[right] = s[right],s[left]                     # Swap the both vowels 
        left+=1                                                 # increment both pointers 
        right-=1
    return ''.join(s)                                           # return the string.

print(reverseVowels("leetcode"))