def Search(nums, target):           # Leetcode : 704
    left, right = 0, len(nums)-1    # here -1 is made to avoid the index out of bound error.
    while(left<=right):             # <= symbol is used, to include last element for search. Try < with the same list given and the target as 9 ( it would return -1 ) 
        mid = (left+right)//2       # find the mid index between left and right index
        if nums[mid]==target:       # if target resides in that mid index, return mid
            return mid
        elif nums[mid]<target:      # elif the number in mid index lesser than target
            left = mid + 1          # increment left pointer, coz the array in sorted in ascending order
        else:                       # else, if the mid value is greater than target
            right = mid - 1         # decrement the right pointer
    return -1                       # if target not found in the array, return -1
nums = [1,2,3,4,5,6,7,8,9]
print(Search(nums, 9))

# Revised Today (5 SEP 2025)