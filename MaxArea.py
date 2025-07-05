def maxArea(height):                            # Leetcode : 11
    l , r = 0 , len(height) - 1                 # create 2 pointers left and right
    m = 0                                       # create a variable to note the max area
    while l < r:                                # use two pointers technique to solve the problem
        minHeight = min(height[l],height[r])    # first we find the minimum height of both the pointers
        area = (r-l) * minHeight                # we use the min height and difference of the indices to find the area

        m = max(area,m)                         # store the maximum area inside m

        if height[l] < height[r]: l+=1          # increment L if the value inside the pointer is smaller than R
        else: r-=1                              # else decrement the R
    
    return m                                    # finally return m

print(maxArea([1,8,6,2,5,4,8,3,7]))