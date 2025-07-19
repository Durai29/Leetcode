def singleNumber(nums):                         # Leetcode : 136
    dic = dict()                                # create a dictionary named dic
    for num in nums:                            # iterate via nums and append the count value of the elements in nums
        if num not in dic:          
            dic[num] = 1
        else:
            dic[num] += 1
    for key,value in dic.items():               # go through the dictionary and return the key which has value as 1.
        if value == 1 : return key
print(singleNumber([2,2,1]))