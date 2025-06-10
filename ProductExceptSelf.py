def productExceptSelf(nums):                    #  Leetcode : 238
    l = len(nums)
    ans = [1]*l                                 # Create a ans array filled with ones, with the len of nums array.

    for i in range(1,l):                        # Iterate the nums array and calculate the product preceding the 
        ans[i] = nums[i-1] * ans[i-1]           # current element and store it in ans[i] (current ans)
                                                # It feels like dynamic programming.
    right = 1
    for i in range(-1,-l-1,-1):                 # Now we can multiply the right product of the element with 
        ans[i] = ans[i] * right                 # the previous left product of that element.
        right *= nums[i]

    return ans

print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([1,2,3,4]))