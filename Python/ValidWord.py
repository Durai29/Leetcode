def isValid(word):                                  # Leetcode : 3136
    vowels = set('aeiouAEIOU')                      # create a set of vowels ( both upper and lower )
    consonants = set('bcdfghjklmnpqrstvwxyz'+
                'bcdfghjklmnpqrstvwxyz'.upper())    # create a set of consonants ( both upper and lower )
    vowelFlag , consFlag = False, False             # create a flag condition for both vowel and consonant
    if len(word) < 3:                               # if the word length is less than 3 : return False 
        return False                                
    for w in word:                                  # iterate the word
        if w in {'@','#','$'}:                      # if you come across any of this symbol return False 
            return False                            # These symbols are given in the constraints
        if w.isalnum():                             # check if it's an digit or alphabet, allow if any
            if w in vowels:                         # check if it's an vowel and update it's flag
                vowelFlag = True
            elif w in consonants:                   # check if it's an consonant and update it's flag
                consFlag = True
    return consFlag and vowelFlag                   # return the and of both flags
    
print(isValid("234Adas"))
print(isValid("b3"))
print(isValid("a3$e"))
print(isValid("Ya$")) 

# Revised today ( 19 JUL 2025 )
# Revised today ( 03 AUG 2025 )