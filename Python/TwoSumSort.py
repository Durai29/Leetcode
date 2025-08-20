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

def twoSum(numbers, target):                                    # Leetcode : 167
    left = 0                                                    # Define left and right pointers    
    right = len(numbers)-1

    while left < right:                                         # use the while loop with condition left < right 
        s = numbers[left] + numbers[right]                      # usually for binary search we use left <= right
        if s == target:                                         # Here we use < only to avoid choosing the same element                    
            return [left+1, right+1]                            # so if s equals target return the values of left + 1  and right + 1
        elif s < target:                                        # if s is lesser, increment target by 1
            left+=1
        elif s > target:                                        # if s is greater, decrement the target by 1
            right-=1
    
print(twoSum([2,7,11,15],9))
print(twoSum([5,25,75],100))

# Revised Today ( 20 AUG 2025 )