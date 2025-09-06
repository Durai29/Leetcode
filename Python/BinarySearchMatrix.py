def searchMatrix(matrix, target):           # Leetcode : 74
    m = len(matrix)                         # number of rows in matrix
    n = len(matrix[0])                      # number of columns in matrix
    left, right = 0, m * n - 1              # initializing left and right pointers
    while left <= right:                    # loop to iterate
        mid = (left + right)//2             # find the mid index
        row = mid // n                      # This is the main part of this problem to covert, Array search to matrix search
        col = mid % n                       # previous line find index of row & this one for col
        if matrix[row][col] == target:      # check if the target is found
            return True                     # if so return True
        elif matrix[row][col] < target:     # else if element is lesser than target, increment left to mid + 1
            left = mid + 1
        else:                               # else decrement right to mid - 1
            right = mid - 1   
    return False                            # if not found return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],6))