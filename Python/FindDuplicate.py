# You must solve the problem without modifying the array nums.
# Use only constant space.

# Use Floyd's Tortoise and Hare (cycle detection) algorithm.

def findDuplicate(nums):            # Leetcode : 287
    slow = 0                        # create 2 pointers
    fast = 0                        # imagine your dealing with a linkedlist
                                    # where nums[n] is the next node n->element in nums
    while True:                     # a infinite loop
        slow = nums[slow]           # one step increment
        fast = nums[nums[fast]]     # two step increment
        if slow==fast:              # if you find any the pointers meet 
            break                   # break the loop
    
    slow2 = 0                       # create a new pointer
    while slow != slow2:            # loop
        slow = nums[slow]           # increment both with one step
        slow2 = nums[slow2]
    return slow                     # break and return if slow == slow2

# Why start from the beginning?
# When slow and fast meet, they are both inside the cycle,
#  but not necessarily at the entrance (the duplicate).
# If you start a new pointer (slow2) at the beginning and 
# move both slow (from meeting point) and slow2 (from start) 
# one step at a time, they will meet at the entrance of the cycle.
# This works because the distance from the start 
# to the entrance is equal to the distance from
#  the meeting point to the entrance (within the cycle).

print(findDuplicate([2,1,3,2]))