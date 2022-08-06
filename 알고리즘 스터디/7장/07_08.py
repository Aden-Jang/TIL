height = [0,1,0,2,1,0,1,3,2,1,2,1]
maxh = max(height)
ans = 0
smaxh = 0
for i in range(len(height)):
    if height[i] < maxh:
        smaxh = max(smaxh, height[i])
        print(smaxh)
        if height[i] > min(maxh, smaxh):
            ans += (height[i] - min(maxh, smaxh))
    # else:
    #     for j in range(i+1,len(height)):
    #         smaxh = max(smaxh, height[j])
    #         if height[i] > min(maxh, smaxh):
    #             ans += (height[i] - min(maxh, smaxh))
print(ans)