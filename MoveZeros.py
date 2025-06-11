def moveZeros(nums):                    #Leetcode : 283
    pos = 0                             # A position variable to swap the non-zero numbers in order.

    for i in range(len(nums)):          # loop to iterate and swap the non-zero numbers.
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    
    for i in range(pos,len(nums)):      # Use the pos variable to fill in the other index with zeros.
        nums[i] = 0
    return nums
print(moveZeros([0,1,0,3,12]))