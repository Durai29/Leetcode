def removeDuplicates(nums):                 # Leetcode : 26
    seen = set()                            # create a seen variable with set datatype.
    i = 0                                   # This is good because, set has O(1) as lookup time. unlike list O(N)
    for num in nums:                        # create i variable to count the unique numbers
        if num not in seen:                 # only allow the num which is not seen
            nums[i] = num                   # swap the unique num with the index in nums list
            seen.add(num)                   # add to seen set
            i+=1                            # increment i
    return nums,i                           # return i
                
print(removeDuplicates([-1,0,0,0,0,3,3]))