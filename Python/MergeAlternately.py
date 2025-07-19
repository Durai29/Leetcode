word1 = "abcdefg"
word2 = "pqr"

def mergeAlternately(word1,word2):              # this is a basic algorithm we could understand I you go through it.
    result = ""
    l1 = len(word1)
    l2 = len(word2)
    m = min(l1,l2)
    for i in range(m):
        result = result + word1[i] + word2[i]

    if (l1 > l2): result = result + word1[m:]
    else: result = result + word2[m:]
    return result
print(mergeAlternately(word1,word2))