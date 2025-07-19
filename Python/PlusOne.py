def plusOne(digits):                                # Leetcode : 66
    multiple = 10                                   # this is helpful in extracting the nums from digits.
    total = 0                                               
    for digit in digits:
        total = (total * multiple) + digit          # get the number from the digits array
    return [int(d) for d in str(total+1)]           # return in the same list form with + 1
print(plusOne([4,3,2,1]))
