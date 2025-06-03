def Search(nums, target):
    left, right = 0, len(nums)-1    # here -1 is made to avoid the index out of bound error.
    while(left<=right):             # <= symbol is used, to include last element for search. Try < with the same list given and the target as 9 ( it would return -1 ) 
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
nums = [1,2,3,4,5,6,7,8,9]
print(Search(nums, 9))
