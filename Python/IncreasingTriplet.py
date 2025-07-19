def increasingTriplet(nums):            # Leetcode : 334
    first = float('inf')                # initialize first with infinity
    second = float('inf')               # initialize second with infinity
    for i in nums:                      # loop through nums.
        if i <= first:                  # only the smallest num will be inside first var.
            first = i   
        elif i <= second:               # code flow will only come here if i > first due to <elif>
            second = i
        else:                           # if the flow comes here there is a third num ( i > second ) that's what we need
            return True                 # so return True
    return False