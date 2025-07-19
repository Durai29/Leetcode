def intToRoman(num):        # Leetcode : 12
    # val = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}  This is slow and doesn't preserve order.
    val = [
            (1000,'M'), (900,'CM'), (500,'D'),                  # list of tuple is better than list of list in performance.
            (400,'CD'), (100,'C'), (90,'XC'),                   # tuples are immutable so, it's good for iteration
            (50,'L'), (40,'XL'), (10,'X'), 
            (9,'IX'), (5,'V'), (4,'IV'),                        # Here the trick is to nums starting with 4 and 9
            (1,'I')
    ]               
    result = ''
    while num > 0:
        for i in range(len(val)):                               # itereate the number and add the corresponding value to the num to result
            if num >= val[i][0]:
                result += val[i][1]
                break
        num -= val[i][0]                                        # subract the number from the num and loop again.
    return result

for i in range(1,500):
    print(intToRoman(i))
print(intToRoman(0))