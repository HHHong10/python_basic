def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(prices[i], min_price)
        max_profit = max(max_profit, prices[i]-min_price)
    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))