prices = [100, 180, 260, 310, 40, 535, 695]
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i-1]
print("Stock Prices:", prices)
print("Maximum Profit:", profit)
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)
lefttallest = [0] * n
lefttallest[0] = heights[0]
for i in range(1, n):
    lefttallest[i] = max(lefttallest[i-1], heights[i])
print("Heights:", heights)
print("Left Tallest:", lefttallest)
righttallest = [0] * n
righttallest[n-1] = heights[n-1]
for i in range(n-2, -1, -1):
    righttallest[i] = max(righttallest[i + 1], heights[i])
print("Right Tallest:", righttallest)
water = 0
for i in range(n):
    water += min(lefttallest[i], righttallest[i]) - heights[i]
print("Total Water Trapped:", water)