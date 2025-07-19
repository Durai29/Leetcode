def findMaxAverage(nums,k):                             # Leetcode : 643
    win_sum = sum(nums[:k])                             # This problem uses sliding window techique.
    max_sum = win_sum                                   # instead of doing the summation in each iteration
                                                        # only the new element to the window is added and the
    for i in range(k,len(nums)):                        # old one is subtracted
        win_sum  = win_sum + nums[i] - nums[k-i]        
        if win_sum > max_sum: max_sum = win_sum         # use if rather than max to reduce the runtime.
    return max_sum/k                                    
print(findMaxAverage([1,12,-5,-6,50,3],4))