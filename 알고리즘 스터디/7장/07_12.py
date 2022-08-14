class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        mina = prices[0]
        for i in prices:
            if i < mina:
                mina = i
            if a < i - mina:
                a = i - mina
        return a


# 시험실행
prices = [7, 1, 5, 3, 6, 4]
a = 0
mina = prices[0]
for i in prices:
    if i < mina:
        mina = i
    if a < i - mina:
        a = i - mina
print(a)

# # 시험실행 - time limit exceeded
# prices = [7, 1, 5, 3, 6, 4]
# a = 0
# for i in range(len(prices)-1):
#     a = max(max(prices[i+1:]) - prices[i], a)
# print(a)

# # 시험실행 - time limit exceeded
# prices = [7, 1, 5, 3, 6, 4]
# a = 0
# for i in range(len(prices)-1):
#     if max(prices[i+1:]) - prices[i] > a:
#         a = max(prices[i+1:]) - prices[i]
# print(a)