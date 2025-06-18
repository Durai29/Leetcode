def findDifference(nums1,nums2):                # Leetcode : 2215
    nums1 = set(nums1)                          # Convert to set datatype
    nums2 = set(nums2)
    c = nums1 & nums2                           # do intersection operation find the common elements
    answer = []
    answer.append(list(nums1-c))                # append the nums1 - common element and convert it to list b4 appending.
    answer.append(list(nums2-c))
    return answer                               # return the answer lol

print(findDifference([1,2,3,3],[1,1,2,2]))