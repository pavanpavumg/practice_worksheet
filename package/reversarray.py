from typing import List
def max_profit_one_transaction(prices: List[int]) -> int:
    max_profit = 0
    min_value = prices[0]
    for index in range(1, len(prices)):
    
    
        if prices[index] < min_value:
            min_value = prices[index]
            continue

        profit = prices[index] - min_value

        if max_profit > profit:
            max_profit = profit
            continue
                
                
    return max_profit
prices = [10, 8, 2, 5, 7, 1, 9]
max_profit_one_transaction(prices)


