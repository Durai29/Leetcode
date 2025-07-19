def reverseWords(s):                    #  Leetcode : 151
    s = s.split()[::-1]                 # split the sentence into single words and store it in a list.
    return ' '.join(s)                  # reverse the list and return in string format using the join method.

print(reverseWords("  hello world  "))