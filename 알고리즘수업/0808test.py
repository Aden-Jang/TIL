'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input())
arr = list(map(int,input().split()))
maxV = arr[0] # 첫 원소를 최대값으로 가정
for i in range(1,N): # 나머지 모든 원소에 대해
    if maxV < arr[i]:
        maxV = arr[i]
print(maxV)