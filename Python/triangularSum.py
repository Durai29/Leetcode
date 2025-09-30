def triangularSum(nums):
    while(len(nums)>1):
        # i = 0
        # j = i+1
        # new_nums =  list()
        # while(j<len(nums)):
        #     new_nums.append((nums[i]+nums[j])%10)
        #     i+=1
        #     j+=1
        new_nums = [(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]
        nums = new_nums
    return nums[0]

print(triangularSum([1,2,3,4,5]))
print(triangularSum([5]))