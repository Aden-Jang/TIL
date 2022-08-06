class Solution:
    def trap(self, height: List[int]) -> int:
        maxh = max(height)
        ans = 0
        smaxh = 0
        # 왼쪽부터 가장 큰 높이까지 반복
        for i in range(height.index(maxh)):
            if height[i] < maxh:
                smaxh = max(smaxh, height[i])
                if height[i] < min(maxh, smaxh):
                    ans += (min(maxh, smaxh) - height[i])
        smaxh = 0
        # 오른쪽부터 가장 큰 높이까지 반복
        for i in range(len(height)-1,height.index(maxh),-1):
            if height[i] <= maxh:
                smaxh = max(smaxh, height[i])
                if height[i] < min(maxh, smaxh):
                    ans += (min(maxh, smaxh) - height[i])
        return ans

'''
# 시험 실행
height = [0,1,0,2,1,0,1,3,2,1,2,1]
maxh = max(height)
ans = 0
smaxh = 0
for i in range(height.index(maxh)):
    if height[i] < maxh:
        smaxh = max(smaxh, height[i])
        if height[i] < min(maxh, smaxh):
            ans += (min(maxh, smaxh) - height[i])
smaxh = 0
for i in range(len(height)-1,height.index(maxh),-1):
    if height[i] <= maxh:
        smaxh = max(smaxh, height[i])
        if height[i] < min(maxh, smaxh):
            ans += (min(maxh, smaxh) - height[i])

print(ans)
'''