def twoSum1(nums, target):               # Leetcode : 1
    seen = {}                           # Dictionary because no redundancy
    for i,num in enumerate(nums):       # Enumerate method is used to extract the indices and the value 
        f = target - num                # find the difference from the target
        if f in seen:                   # find the subracted value in seen ( Dictionary )
            return [i,seen[f]]          # return the indices if there is a match.
        seen[num] = i                   # store the value in the dictionary
# print(twoSum([2,7,11,15], 9))
print(twoSum1([3,2,4],6))
# print(twoSum([3,3],6))
print(twoSum1([-1,-2,-3,-4,-5],-8))

def twoSum2(nums, target):              # Leetcode : 1
    dic = dict()                        
    for i, num in enumerate(nums):      
        f = target - num                # this is the crucial step to find the number from the differnce from target
        if f in dic:                    # now to avoid the summation of same number this step helps us
            return [dic[f], i]          # only we would return if find is inside the dictionary
        dic[num] = i                    # else add it to the dictionary


print(twoSum2([3,2,4],6))