def canPlaceFlowers(flowerbed, n):                                  # Problem : 605
    if n==0: return True                                            # Special case if n == 0
    for i in range(len(flowerbed)):                                 # Iterate with range len(flowerbed)
        if flowerbed[i]==0:                                         # only allow the not planted flowerbed (0) 
            left = (i==0) or flowerbed[i-1]==0                      # conditon for empty left
            right = i==len(flowerbed)-1 or flowerbed[i+1]==0        # conditon for empty right
            if left and right:                                      # if both left and right are true
                 flowerbed[i] = 1                                   # change the i th index to 1 
                 n-=1                                               # decrement n
                 if n==0:                                           # Break if n==0, this is a special case where n may be lesser than the available empty slots
                     return True
    return False

print(canPlaceFlowers([0,1,0,1,0,1,0,0],1))
