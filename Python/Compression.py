def compression(chars):                                        # Leetcode : 443
    read = 0
    write = 0                                                  # Here we use two-pointers technique to solve this prob

    while read < len(chars):                                   # loop through the chars list
        char = chars[read]      
        count = 0
        while read < len(chars) and chars[read] == char:       # This is the place where the magic of 2 pointers
            count += 1
            read += 1                                          # count the num of read and count the chars
        chars[write] = char                                    # replace the characters in char list           
        write += 1                                             # increment write
        if count > 1:                                          # allow only if count is greater than 1
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write                                               # return the write varible
print(compression(list('aaaabbbb')))