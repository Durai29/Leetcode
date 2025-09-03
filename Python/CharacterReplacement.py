def characterReplacement(s,k):                      # Leetcode : 424
    dic = dict()                                    # dictionary to keep track of frequency of elements
    left = 0                                        # Left pointer of sliding window
    res = 0                                         # final result which has max substring length
    m = 0                                           # temp max value in the dictionary
    for right in range(len(s)):                     # now we use a loop to iterate the given string
        dic[s[right]] = dic.get(s[right],0) + 1     # this finds the frequency of an element, and this get
                                                    # method returns value if key exists or return 0
        m = max(m, dic[s[right]])                   # finds the max frequency from the dictionary
        while ((right - left + 1) -  m) > k:        # loop to check the condition is valid (atmost k times - element replacement)
            dic[s[left]] -= 1                       # if so shrink the window by decreasing the value of left pointer
            left += 1                               # and increament the left pointer

        res = max(right - left + 1, res)            # finally keep track of max window size.
    return res                                      # return res
        
print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBAB",2))