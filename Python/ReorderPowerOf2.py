def reorderPowerOf2(n):                         # Leetcode : 869
    digits = sorted(str(n))                     # sort the number after converting to string
    for i in range(31):                         # 2^30 is within 10^9
        if sorted(str(1 << i)) == digits:       # Use bitwise operator to shift left and find the powers of 2
            return True                         # if a number is found to be same with digits return true
    return False                                # else return false
    # num = str(n)
    # all_num = []
    # s = set()
    # def permutate(num_count,char,s):
    #     if num_count == len(num):
    #         all_num.append(char)
    #         return
    #     for i in range(len(num)):
    #         if i not in s:
    #             s.add(i)
    #             permutate(num_count+1,char+str(num[i]),s)
    #             s.remove(i)
    # permutate(0,'',s)
    # for i in all_num:
    #     bin_num = bin(int(i))[2:]
    #     if bin_num.count('1') == 1 and str(i)[0]!='0':
    #         return True
    # return False

    # num = str(n)
    # used = set()
    # found = [False]
    # def permutate(path):
    #     if len(path) == len(num):
    #         if path[0] != '0':
    #             number = int(path)
    #             if number & (number - 1) == 0:
    #                 found[0] = True
    #         return
    #     for i in range(len(num)):
    #         if i not in used:
    #             used.add(i)
    #             permutate(path+num[i])
    #             used.remove(i)
    #         if found[0]:
    #             return
    # permutate('')
    # return found[0]


print(reorderPowerOf2(128))        
print(reorderPowerOf2(46))        
print(reorderPowerOf2(10))        
print(reorderPowerOf2(56635))        