def validAnagram(s,t):              # Leetcode : 242
    if len(s) != len(t):            # return False if the length of both the strings are different.
        return False
    dic1 = {}                       # create 2 dictionaries to count the frequency
    dic2 = {}
    def count(dic,st):              # define a function to count the frequency
        for i in st:
            if i not in dic:
                dic[i] = 1
            else: 
                dic[i] += 1
    count(dic1,s)               
    count(dic2,t)
    return dic1 == dic2             # return true if both are same.
            
print(validAnagram("anagram","nagaram"))