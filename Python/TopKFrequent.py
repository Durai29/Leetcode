def topKFrequent(nums,k):                                           # Leetcode : 347
    dic = dict()                                                    # create a dictionary
    for num in nums:                                                # note the frequency of the element
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    temp = sorted(dic.items(), key= lambda x: x[1], reverse=True)   # sort the dictionary with the frequency as key in descending order
    result = list()                                                 # create a list
    for i in range(k):                                              # loop through k number of times to find top k frequent element
        result.append(temp[i][0])                                   # append the first k elements ( note the list is in descending order)
    return result                                                                           
print(topKFrequent([1,1,1,2,2,3],2))