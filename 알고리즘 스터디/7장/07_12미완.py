


# 시험실행
prices = [7, 1, 5, 3, 6, 4]
maxp = max(prices)


# 시험실행 - time limit exceeded
prices = [7, 1, 5, 3, 6, 4]
a = 0
for i in range(len(prices)-1):
    a = max(max(prices[i+1:]) - prices[i], a)
print(a)

# 시험실행 - time limit exceeded
prices = [7, 1, 5, 3, 6, 4]
a = 0
for i in range(len(prices)-1):
    if max(prices[i+1:]) - prices[i] > a:
        a = max(prices[i+1:]) - prices[i]
print(a)