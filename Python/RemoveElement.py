def removeElement(nums,val):                            # Leetcode : 27
    # l = 0                                             # First I tried to solve this problem with 2 pointers
    # r = len(nums) - 1
    k = 0                                               
    # while l < r:                                      # this is a boilerplate code for the two pointers problem
    #     while l < r and nums[l] != val:
    #         l += 1
    #     while l < r and nums[r] == val:
    #         r -= 1
    #     if nums[l] != nums[r]:
    #         nums[l] , nums[r] = nums[r] , nums[l]     # but there were many failures in the testcases so I moved to this simple solution
    #         k += 1
    # if k==0: return 0
    # else: return len(nums)-k
    for i in nums:                                      # Here we loop through each element in nums
        if i != val:                                    # if a element the list not equals the val
            nums[k] = i                                 # then make the element in k position
            k+=1                                        # increment k
    return k                                            # finally return k

# Two pointers method:
def removeElement2(nums,val):                           # leetcode : 27
    i = 0                                               # create left pointer i
    n = len(nums)                                       # right pointer n
    while i < n:                                        # loop to go through the list
        if nums[i] == val:                              # if the left pointer has the val
            nums[i] = nums[n - 1]                       # swap it to the right pointer
            n -= 1                                      # and decrement n
        else:                                           # else increment left pointer and move on
            i += 1
    return n                                            # finally return n

# Test cases :
print(removeElement2([0,1,2,2,3,0,4,2], 2))        # Expected: 5
print(removeElement2([3,2,2,3], 3))               # Expected: 2
print(removeElement2([1], 1))                    # Expected: 0
print(removeElement2([4,5], 4))                  # Expected: 1
print(removeElement2([3,3,3,3], 3))              # Expected: 0
print(removeElement2([], 0))                    # Expected: 0
print(removeElement2([2,2,2,1,2,3,4], 2))        # Expected: 3
print(removeElement2([1,2,3,4,5], 6))            # Expected: 5
print(removeElement2([2,2,2], 1))                # Expected: 3
print(removeElement2([2,2,2], 2))                # Expected: 0