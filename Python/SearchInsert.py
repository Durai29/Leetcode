def searchInsert(nums,target):      # Leetcode : 35 
    l = 0                           # create a left pointer
    r = len(nums) - 1               # create a right pointer
    while l <= r :                  # here we use binary search algorithm
        m = (l+r)//2                # find the mid index
        if nums[m] == target:       # if m equals target return m
            return m
        elif nums[m] < target:      # if lesser change l to m + 1
            l = m + 1
        else:                       # if greater change r to m - 1
            r = m - 1
    return l                        # return L " L is the lowest index where target can be inserted without breaking the sort order. "

print(searchInsert([1,3,5,6], 5))  # Should return 2 (found)
print(searchInsert([1,3,5,6], 2))  # Should return 1 (insert at index 1)
print(searchInsert([1,3,5,6], 7))  # Should return 4 (insert at end)
print(searchInsert([1,3,5,6], 0))  # Should return 0 (insert at start)

# Revised Today ( 04 AUG 2025 )
# Revised Today ( 11 AUG 2025 )