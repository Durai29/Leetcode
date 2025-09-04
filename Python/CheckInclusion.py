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

def checkInclusion(s1,s2):                      # Leetcode : 567
    n = len(s1)                                 # length of string 1
    m = len(s2)                                 # lenght of string 2
    
    dic1 = dict()                               # dictionary 1 to maintain the frequency of string 1
    for i in range(len(s1)):                    # extracts the frequency of each element in string 1
        dic1[s1[i]] = dic1.get(s1[i],0) + 1

    dic2 = dict()                               # dictinary 2 to maintain the frequency of the first n
    for i in s2[:n]:                            # elements of string 2.
        dic2[i] = dic2.get(i,0) + 1

    if dic1 == dic2:                            # if both dictionaries are equal return True
        return True
    
    for i in range(n,m):
        dic2[s2[i]] = dic2.get(s2[i],0) + 1     # add the next character from string 2 

        dic2[s2[i-n]] -= 1                      # remove the left most character in the window
        if dic2[s2[i-n]] == 0:                  # if a element becomes 0 delete the key:value pair
            del dic2[s2[i-n]]

        if dic1 == dic2:                        # check if the new dictionary and dic1 are equal
            return True                         # if so return True
        
    return False                                # else return False

print(checkInclusion("ab","eidbaooo"))