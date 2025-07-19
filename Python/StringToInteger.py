def myAtoi(s):                                              # Leetcode : 8
    s = s.strip()                                           # remove leading and trailing spaces
    if s == '': return 0                                    # return if empty string
    msign = True if s[0]=='-' else False                    # take note of - sign and + sign
    psign = True if s[0]=='+' else False
    result = '0'                                            # assign 0 as default result
    if msign or psign: s = s[1:]                            # ignore if sign exists
    for char in s:          
        if char.isdigit():                                  # append only the digits to the result
            result += char
        else:                                               # if non digits exists break the loop
            break
    if msign: result = '-' + result                         # add minus if psign is true to the result
    result = int(result)
    if result < -2**31: result = -2**31                     # round the number as defined int the question
    if result > (2**31)-1 : result = (2**31)-1
    return result
print(myAtoi("  -042"))
print(myAtoi('42'))
print(myAtoi("1337c0d3"))
print(myAtoi('0-1'))
print(myAtoi("words and 987"))