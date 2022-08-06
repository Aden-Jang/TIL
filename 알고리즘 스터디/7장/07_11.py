class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fnum = [1]
        lnum = [1]
        ans = []
        # 0 ~ nums의 개수 -1 만큼의 1씩 증가할 때마다 곱 리스트 
        for i in range(0,len(nums)-1):
            fnum.append(fnum[i]*nums[i])
        # nums의 개수 -1 ~ 0 만큼의 1씩 감소할 때마다 곱 리스트 
        for i in range(len(nums)-1,0,-1):
            lnum.append(lnum[len(nums) - i - 1]*nums[i])
        # 위 두개 리스트를 크로스로 곱
        for i in range(len(fnum)):
            ans.append(fnum[i]*lnum[-i-1])
        return ans

'''
# 시험실행
nums = [1, 2, 3, 4]
fnum = [1]
lnum = [1]
ans = []
for i in range(0,len(nums)-1):
    fnum.append(fnum[i]*nums[i])
for i in range(len(nums)-1,0,-1):
    lnum.append(lnum[len(nums) - i - 1]*nums[i])
for i in range(len(fnum)):
    ans.append(fnum[i]*lnum[-i-1])
print(ans)
'''

'''
# 시험실행 - time limit exceeded
nums = [1, 2, 3, 4]
ans = []
for i in range(len(nums)):
    ansnum = 1
    for j in range(i):
        ansnum *= nums[j]
    for k in range(i+1,len(nums)):
        ansnum *= nums[k]
    ans.append(ansnum)
print(ans)
'''