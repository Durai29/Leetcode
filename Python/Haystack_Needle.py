def strStr(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):    # Here len(haystack)-len(needle) is used to avoid the index out of 
                                                    # bound error, while we slide the window (needle) throught the haystackOB
        if not needle:
            return 0
        if haystack[i:i+len(needle)]==needle:       # This is where the window is created (string slicing)
            return i
    return -1

print(strStr("catdogcat","dog"))
