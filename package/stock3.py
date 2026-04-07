from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = float('inf')
        s1 = 0
        b2 = float('inf')

        s2 = 0
        

        for price in prices:
            b1 = min(b1, price)
            s1 = max(s1, price - b1)

            b2 = min(b2, price - s1)
            s2 = max(s2, price - b2)

        return s2
stock = Solution()
prices = [3,3,5,0,0,3,1,4]
print(stock.maxProfit(prices))