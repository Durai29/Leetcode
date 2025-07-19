def productExceptSelf1(nums):                    #  Leetcode : 238
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

def productExceptSelf2(nums):                               # Leetcode : 238
    prodL = [1]*len(nums)                                   # create 2 arrays
    prodR = [1]*len(nums)                                   # to monitor the product of element left and right to it
    for i in range(1,len(nums)):
        prodL[i] = prodL[i-1] * nums[i-1]                   # find the left product
    for i in range(len(nums)-1,0,-1):
        prodR[i-1] = prodR[i] * nums[i]                     # find the right product
    return [prodR[i]*prodL[i] for i in range(len(nums))]    # return the product of both prodL and prodR

print(productExceptSelf1([1,2,3,4]))
print(productExceptSelf2([-1,1,0,-3,3]))
print(productExceptSelf1([1,2,3,4]))