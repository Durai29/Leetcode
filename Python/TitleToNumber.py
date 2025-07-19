def titleToNumber(word):        # It's a basic Leetcode (171) problem.
    c = 1                       
    num = 0
    for i in word[::-1]:        # Access the string in reverse 
        value = ord(i) - 64     # Get the ASCII value and subtract with 64 to get the numerical order number.
        num += value * c        # Multiply with 26 just like we do in the binary and decimal (ones, tens, hundreds) - (26,26^2,...)
        c *= 26
    return num

print(titleToNumber("ZY"))