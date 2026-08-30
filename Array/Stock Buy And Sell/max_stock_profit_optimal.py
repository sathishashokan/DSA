# Brute Force
# def max_stock_profit(prices):
#     n = len(prices)
#     max_profit = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             profit = prices[j] - prices[i]
#             max_profit = max(max_profit, profit)
#     return max_profit


def max_stock_profit(nums):
    maxi = 0
    min_price = float('inf')

    for num in nums:
        if num < min_price:
            min_price = num

        profit = num - min_price
        if profit > maxi:
            maxi = profit

    return maxi

arr = [7,6,4,3,1]
arr1 = [7,2,4,1,1]
arr2 = [7,1,5,3,6,4]
print(max_stock_profit(arr1))