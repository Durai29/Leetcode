def majorityElement(nums):                          # Leetcode : 169
    dic = dict()                                    # creat a dictionary
    for i in nums:                                          
        if i not in dic:                            # get the frequency of the elements
            dic[i] = 1
        else:
            dic[i] += 1
    c = 0
    for k,v in dic.items():                         # find the element with maximum frequency and return it.
        if c < v:
            m = k
            c = v
    return m
print(majorityElement([1,5,1,2,4,2,1,4,5,5,1]))