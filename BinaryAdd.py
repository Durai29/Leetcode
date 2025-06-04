a = '11'
b = '01'

def addBinary(a,b):
    a = int(a,2)            # convert the string of binary num to int of decimal format using the parameter (a,2) {a->str}
    b = int(b,2)
    return bin(a+b)[2:]     # return the result of the int addition, converted in binary form. We slice out the  0b in  0b100 (result)
print(addBinary(a,b))