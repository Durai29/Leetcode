def threeSum(nums):                             # Leetcode : 15
    nums.sort()                                 # sort the array in ascending order
    result = []                                 # create a result list to store all unique triplets
    for i in range(len(nums)):                  # use a for loop to traverse the list with index variable "i"
        if i > 0 and nums[i] == nums[i-1]:      # skip duplicate values for "i" to avoid repeating triplets
            continue
        l, r = i + 1, len(nums) - 1             # initialize two pointers: l = i+1 (left), r = last index (right)
        while l < r:                            # continue until the two pointers meet
            s = nums[i] + nums[l] + nums[r]     # calculate the sum of the current triplet
            if s == 0:                          # if the sum equals 0, we found a valid triplet
                result.append([nums[i], nums[l], nums[r]])   # add the triplet to the result list
                l += 1                          # move the left pointer forward
                r -= 1                          # move the right pointer backward
                while l < r and nums[l] == nums[l - 1]:      # skip duplicate values for l
                    l += 1
                while l < r and nums[r] == nums[r + 1]:      # skip duplicate values for r
                    r -= 1
            elif s < 0:                         # if the sum is less than 0, we need a bigger number
                l += 1                          # move the left pointer forward
            else:                               # if the sum is greater than 0, we need a smaller number
                r -= 1                          # move the right pointer backward
    return result                               # return the final list of triplets

# Example usage
print(threeSum([-1, 0, 1, 2, -1, -4]))          # expected output: [[-1, -1, 2], [-1, 0, 1]]

# Revised Today ( 27 AUG 2025 )