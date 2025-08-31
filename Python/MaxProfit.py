import numpy as np                                      # Leetcode : 121
                                                        # import numpy for using infinity.
def maxProfit(prices):                                  
    min_price = np.inf                                  # here we use inf to find the min val at first
    max_profit = 0                                      # decalre a max_profit variable.
    for i in prices:                                    # so, each day we need to calculate min_price and current_profit and max_profit.
        min_price = min(min_price,i)                    # check if today's price is the min_price
        current_profit = i - min_price                  # calculate the today's profit
        max_profit = max(max_profit, current_profit)    # and check which has the max profit

    return max_profit                                   # return the max_profit

print(maxProfit([7,1,5,3,6,4]))