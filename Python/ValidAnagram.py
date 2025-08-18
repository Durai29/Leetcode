# Method 1 : Hashing  O(N)              
def validAnagram1(s,t):             # Leetcode : 242
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
            
# Method 2 : sorting   O(NlogN)
def validAnagram2(s,t):                 # Leetcode : 242 
    if len(s)!= len(t): return False    # return False if length are not same.
    s = list(s)                         # convert both the string to list
    t = list(t)
    s.sort()
    t.sort()                            # sort them in ascending order ( it takes nlogn time)
    return s==t                         # check both s and t are same after sorting.

# Method 3: fixed array     O(N)
def validAnagram3(s,t):                     # Leetcode : 242 
    if len(s)!=len(t): return False         # return False if length are not same.    
    count = [0] * 26                        # create a fixed list of length 26 
    for ch1,ch2 in zip(s,t):                # zip both the string to iterate in a single loop.
        count[ord(ch1) - ord('a')] += 1     # find the index of the alphabet and count it
        count[ord(ch2) - ord('a')] -= 1     # like wise decrement the count if it's found in the second string
    return all(i==0 for i in count)         # return True if all the values in count array is 0

print(validAnagram3("anagram","nagaram"))

# Revised Today ( 18 AUG 2025 )