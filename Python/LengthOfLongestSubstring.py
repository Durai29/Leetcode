def lengthOfLongestSubstring(s):            # Leetcode : 03
    win = set()                             # create a set to maintain the win
    m = 0                                   # create variable m to have count of max substring
    left = 0                                # use left and right pointer to implement the variable sliding window technique
    for right in range(len(s)):             # Here we, use right pointer directly in the for loop as iterative variable.
        while s[right] in win:              # Now if there is a duplicate in the window, we should shrink the window from left to eliminate the duplicates 
            win.remove(s[left])             # so remove the left most element in the window  
            left += 1                       # and increment the left pointer
        win.add(s[right])                   # this step happens everytime when there is an increment (right)
        m = max(m,right-left+1)             # Find the max substring length and store it in variable m
    return m                                # Finally return m
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
