def twoSum(nums, target):               # Leetcode : 1
    seen = {}                           # Dictionary because no redundancy
    for i,num in enumerate(nums):       # Enumerate method is used to extract the indices and the value 
        f = target - num                # find the difference from the target
        if f in seen:                   # find the subracted value in seen ( Dictionary )
            return [i,seen[f]]          # return the indices if there is a match.
        seen[num] = i                   # store the value in the dictionary
# print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4],6))
# print(twoSum([3,3],6))
print(twoSum([-1,-2,-3,-4,-5],-8))