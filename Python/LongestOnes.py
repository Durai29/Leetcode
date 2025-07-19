def longestOnes(nums, k):                # Leetcode : 1004
    left = 0
    max_len = 0
    zeros = 0

    for right in range(len(nums)):       # Iterate through the nums with right instance.
        if nums[right] == 0:             # increment zero if num[right] is 0
            zeros += 1

        while zeros > k:                 # if zero > k , it means the current window 
            if nums[left] == 0:          # size is greater than k, we need to shift 
                zeros -= 1               # left and shrink the window size to k
            left += 1

        max_len = max(max_len, right - left + 1)  # find the max of max_len and the 
                                                  # distance between right and left + 1
                                                  # + 1 is coz of the index num from 0
    return max_len


print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))