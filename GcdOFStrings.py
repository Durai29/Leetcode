import math
def gcdOfStrings(str1,str2):                        # Problem : 1071
    if str1 + str2 != str2 + str1: return 'NONE'    # Here we check if there is a pattern repetition.

    x = math.gcd(len(str1),len(str2))               # We calculate the gcd of both the string length and find the pattern's length,
    return str1[:x]                                 # as we confirmed that there is a pattern in the above condition.
                                                    # Finally return the pattern with it's lenght sliced from a string.
print(gcdOfStrings('ABCABC','ABC'))