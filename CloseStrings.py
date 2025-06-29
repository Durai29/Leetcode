def closeStrings(word1, word2):                             # Leetcode :  1657
    set1 = set(word1)                                       
    set2 = set(word2)
    if set1 != set2: return False                           # check if both words have the same number of elements
    count1 = sorted(word1.count(char) for char in set1)     
    count2 = sorted(word2.count(char) for char in set2)
    return count1 == count2                                 # count the frequency of the elements and return True or False.

print(closeStrings('abc','cba'))