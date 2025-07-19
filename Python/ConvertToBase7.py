def convertToBase7(num):                    # Leetcode : 504
    if num == 0:                            # if the num is 0 return 0 ( base case or special case )
        return '0'
    result = str()                          # create a result variable
    sign = True if num < 0 else False       # flag the sign variable to indicate negative sign
    num = abs(num)                          # make the num positive        
    while num > 0:                          
        result = str(num % 7) + result      # append the modulo of the num in front of the result 
        num //= 7                           # divide the num with 7 and store it in num
    if sign : result = '-' + result         # add an minus if the sign is True, to result
    return result
print(convertToBase7(-7))