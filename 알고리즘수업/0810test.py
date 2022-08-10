N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
'''
3
1 2 3
4 5 6
7 8 9
'''
print(arr)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
'''
3
123
456
789
'''
print(arr)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

N, M = map(int,input().split())
arr = [list(map(int, input())) for _ in range(N)]
'''
2 4
1 2 3 4
5 6 7 8
'''
print(arr)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k] # *숫자를 써주면 숫자만큼 인접한 거리를 나타냄
            nj = j + dj[k] # *숫자를 써주면 숫자만큼 인접한 거리를 나타냄
            if 0<=ni<N and 0<=nj<M:
                print(ni,nj)

arr = [7, 2, 5, 3, 4, 6]
N = len(arr)
for i in range(N-1):
    minIdx = i # 구간의 맨 앞을 최소값으로 가정
    for j in range(i+1, N): # 실제 최소값 인덱스 찾기
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx] # 최소값을 구간 맨 앞으로 이동
print(arr)