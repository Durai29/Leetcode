def threeSum(nums):                                         # Leetcode : 15
    nums.sort()                                             # sort the array in ascending order
    result = []                                             # create a result list
    for i in range(len(nums)):                              # now use a for loop to traverse the list with index variable "i"
        l , r = i+1 , len(nums)-1                           # here 2 variables are created l = i+1 and r = len(nums)-1
        while l < r:                                        # here the two pointer technique is used search other 2 numbers
            s = nums[i] + nums[l] + nums[r]                 # summation is made here
            if s == 0:                                      # if sum equals 0 add the elements to list and move to next i term
                result.append([nums[i],nums[l],nums[r]])
                break                                       # break is important
            elif s < 0:                                     # if it's lesser than 0 increment L   
                l += 1
            elif s > 0:                                     # if it's greater than 0 decrement R
                r -= 1 
    return result                                           # return result

print(threeSum([-1,0,1,2,-1,-4]))