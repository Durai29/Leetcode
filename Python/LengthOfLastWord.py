word = "   Hello    World   "

def lengthOfLastWord(word):             # This is another basic problem.
    word = word.strip()                 # strip() method is used to erradicate the trailing spaces.
    count = 0                           
    for i in word[::-1]:                # string is accessed in reverse order and the no.of letters are counted.
        if i==' ': break
        else: count+=1
    return count
print(lengthOfLastWord(word))