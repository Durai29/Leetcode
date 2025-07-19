def uniqueOccurences(arr):              # Leetcode : 1207
    d = dict()                          # create a dictionary to count the number of elements
    for i in arr:                       # fill in the frequency of the elements
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)                            
    l = list(d.values())                # extract the values list 
    for i in range(len(d)):             # iterate them to find duplicates.
        for j in range(i+1,len(d)):     # here i+1 is important because same element shouldn't be considered.
            if l[i] == l[j]:
                return False
    return True

print(uniqueOccurences([1,2,2,1,1,3]))