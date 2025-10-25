# Leetcode : 1716
class Solution:
    def totalMoney(self, n: int) -> int:
        weekDays = 7
        cycle = n // weekDays
        remainder = n % weekDays
        total = 0
        for w in range(cycle):
            total += 7 * (w + 1) + 21

        for i in range(remainder):
            total += cycle + 1 
            cycle += 1
        return total