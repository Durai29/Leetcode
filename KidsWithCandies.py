def kidsWithCandies(candies, extraCandies):         # Problem : 1431
        l = len(candies)
        result = [True] * l                         # Initialize the result array
        m = max(candies)                            # get the max element from the candies array
        for i in range(l):
            if candies[i] + extraCandies < m:       # Check If the each kid has more candies than the max 
                result[i] = False                   # if not make it false

        return result                               # return the result.                      

print(kidsWithCandies([4,2,1,1,2],1))
