class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stackt[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


# temperatures = [15, 16, 12, 13, 18]
# ans = []
# for i in range(len(temperatures)-1):
#     ansx = 1
#     for j in range(i+1, len(temperatures)):
#         if j == len(temperatures) - 1 and temperatures[i] >= temperatures[j]:
#             ansx = 0
#             break
#         elif temperatures[i] < temperatures[j]:
#             break
#         else:
#             ansx += 1
#     ans.append(ansx)
# ans.append(0)
# print(ans)