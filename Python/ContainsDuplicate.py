# Method 1: O(N) - recommended
def containsDuplicate1(nums):                       # Leetcode : 217
    seen = set()                                    # declare a set to mark the seen elements
    for num in nums:                                # go throught the array to find add elements to seen 
        if num not in seen:             
            seen.add(num)
        else:                                       # if a seen element is found again return True
            return True
    return False

# Method 2: O(N)
def containsDuplicate2(nums):                       # Leetcode : 217
    dic = {}                                        # create a dictionary
    for num in nums:                                
        if num not in dic:
            dic[num] = 1                            # extract the frequency of elements out of nums
        else:
            dic[num] += 1
    return not all(i==1 for i in dic.values())      # find if there any duplicates with all function

# Method 3: O(N log N)
def containsDuplicate3(nums):                       # Leetcode : 217
    nums.sort()                                     # sort the array
    for i in range(1,len(nums)):                    # go through all elements of sorted array
        if nums[i] == nums[i-1]:                    # if 2 adjacent elements are equal return True
            return True
    return False                                    # else return False

print(containsDuplicate3([1,2,3,1]))

# Revised Today ( 19 AUG 2025 )