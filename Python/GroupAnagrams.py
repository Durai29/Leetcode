def groupAnagrams(strs):                                        # Leetcode : 49
    new = [''.join(sorted(i)) for i in strs]                    # sort the strings inside strs and again convert them to string
    dic = dict()                                                # create a dictionary 
    for i,j in zip(strs,new):                                   # use zip method to iterate both lists ( both list are of same length )
        if j not in dic:                                        # if key not present add to the dictionary value list
            dic[j] = [i]
        else:                                                   # if present append the value
            dic[j].append(i)
    return list(dic.values())                                   # return the list of values
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))