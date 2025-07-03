def isValidSudoku(board):                           # Leetcode : 36 
    # checks row
# ------------------------------------- #
    for row in board:                               # goes through each row of the board
        seen = set()                                # here set is created to manage the seen elements
        for i in row:                               
            if i not in seen:                       # if element not present in seen add it to seen
                    seen.add(i)
            else:
                if i != '.':                        # if any other element other than '.' is present in seen return False
                    return False
# ------------------------------------- #
 
    # checks column
# ------------------------------------- #                
    for col in range(len(board)):                   # now we traverse the board in columns 
        seen = set()                                # another set is created to again keep track of seen elements
        for row in range(len(board)):               
            if board[row][col] not in seen:         # if element not found in seen add it to seen
                seen.add(board[row][col])
            else:
                if board[row][col] != '.':          # if a element is seen again other than '.' return False
                    return False 
# ------------------------------------- #

    # checks inner box : method 1 ( Recommended )
# ------------------------------------- #           # The inner small box is the tricky part
    for i in range(9):                              # here we loop through the range of 9
        seen = set()                                # again another set
        for j in range(9):                          
            row = 3 * (i // 3) + (j // 3)           # here is the magic happens, we use this formula to derive the indices to traverse
            col = 3 * (i % 3) + (j % 3)             # this is for column
            if board[row][col] not in seen:         # same seen set is used to find any duplicates
                seen.add(board[row][col])
            else:                                   # the only difference in row in col formula is the // (floor division) and % (remainder)
                if board[row][col] != '.':
                    return False
    return True
# ------------------------------------- #

#     # checks inner box : method 2
# # ------------------------------------- #               # This is another alternate way 
#     for i in [0,3,6]:                                 # Here we go through 0,3,6 list 
#         for j in [0,3,6]:                             # we traverse this to find the starting indices of the first box in each small boxes (3 x 3)
#             seen = set()  
#             for row in range(i, i+3):                 # And here in this real traversal takes place
#                 for col in range(j, j+3):             # both row and col are found in this two loops
#                     if board[row][col] not in seen:
#                         seen.add(board[row][col])     # then we can find our duplicates from our seen set method.
#                     else:
#                         if board[row][col] != '.':
#                             return False
#     return True
# # ------------------------------------- #
    
        
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))