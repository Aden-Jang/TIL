class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans += min(nums[i], nums[i+1])
        return ans

'''
# 시험 실행
nums = [1, 4, 3, 2]
nums.sort()
ans = 0
for i in range(0,len(nums),2):
    ans += min(nums[i], nums[i+1])
print(ans)
'''