# 시험실행 - time limit exceeded
nums = [-1, 0, 1, 2, -1, -4]
a=[]
nums = sorted(nums,reverse=False)
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)-0):
        if -(nums[i] + nums[j]) in nums[j+1:]:
            a.append((nums[i], nums[j], -(nums[i] + nums[j])))
print(list(set(a)))