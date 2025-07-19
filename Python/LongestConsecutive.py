def longestConsecutive(nums):                       # Leetcode : 128
    s = set(nums)                                   # create a set : set datatype has O(1) of lookup time
    longest = 0                                     # have a count of the longest consecutive numbers
    for num in s:                                   # iterate through the set
        if num-1 not in s:                          # find the first number of the consecutive numbers
            current = num                           # make it as the current number
            streak = 1                              # here streak is set to 1 because we have found out the first number of the consecutive numbers
            while current+1 in s:                   # scan through all the consecutive numbers
                current += 1                        # increment current
                streak += 1                         # take note of streaks
            longest = max(streak,longest)           # assign the longest with the maximum streak
    return longest                                  # return longest
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([-5,-2,0,1,2,3,4,100]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))