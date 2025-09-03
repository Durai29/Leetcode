def checkInclusion(s1, s2):                     # Leetcode : 567
    left = 0                                    # left pointer
    right = len(s1)                             # right pointer
    dic1 = dict()                               # dictionary to maintain the frequency of s1
    for i in s1:                                # finds the frequency 
        dic1[i] = dic1.get(i,0) + 1
    while right <= len(s2):                     # real loop to slide throught s2
        dic = dict()                            # internal dictionary to find the frequency of the window
        for i in s2[left:right]:                # this line finds the frequency of window
            dic[i] = dic.get(i,0) + 1
        if dic == dic1:                         # if both are same return True
            return True
        left += 1
        right += 1
    return False                                # if loop terminates return False

# print(checkInclusion("air","durai"))
print(checkInclusion("hello","ooolleoooleh"))