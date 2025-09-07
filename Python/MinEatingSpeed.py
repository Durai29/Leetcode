def minEatingSpeed(piles,h):                                # Leetcode : 875
    low = 1                                                 # low pointer as 1, coz the min speed. (1 bananna per hour)
    high = max(piles)                                       # high pointer as max bananna in the pile. Max speed for Koko to eat per hour.
    while low <= high:                                      # while loop with low <= high condition
        mid = (low + high) // 2                             # find the mid speed    
        hour = sum((p + mid - 1) // mid for p in piles)     # this is the crucial formula to find the hours taken by Koko to complete eating the pile with "mid" speed
                                                            # here (p + mid - 1) is done because, we need to convert the value to next integer if there is a floting point
        if hour <= h:                                       # so, next we check whether the hour we calculated is lesser than the give "h"
            right = mid - 1                                 # if so Koko's speed is too high, we need to reduce it. That's why we decrement high to mid - 1
        else:                                               # else the hour is greater increase the lower bound by  mid + 1
            left = mid + 1
    return low                                              # Finnaly return the lower bound coz that's the min speed koko must eat the bananna's to complete the pile within the give time

print(minEatingSpeed([3,6,7,11],8))