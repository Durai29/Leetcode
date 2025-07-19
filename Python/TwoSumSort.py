def twoSumSort(numbers, target):                                # Leetcode : 167    
    l , r = 0 , len(numbers) - 1                                # Two pointers
    while l < r:                                                # two pointers boilerplate
        while l < r and (numbers[l] + numbers[r]) < target:     # this is a sorted list so we can apply this logic
            l += 1                                              # increment left if sum is lesser than target
        while l < r and (numbers[l] + numbers[r]) > target:     # decrement right if sum is greater than target
            r -= 1
        
        if numbers[l] + numbers[r] == target:                   # if sum equals target return the indices + 1
            return [l+1, r+1]
    
print(twoSumSort([2,7,11,15],9))    