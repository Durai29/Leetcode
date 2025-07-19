def convertToTitle(num):
    char = ''
    while num>0:
        num-=1
        remainder = num % 26
        char = chr(ord('A') + remainder) + char
        num//=26

    return char

print(convertToTitle(701))