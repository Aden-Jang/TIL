# 풀었는데 시간초과로 실패
# 해당 인덱스부터 그이후를 max로 쓰다보니 시간이 오래걸린 것 같음
'''
T = int(input())
for i in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    b = 0
    for j in range(N):
        if a[j] < max(a[j:N+1]):
            b += max(a[j:N+1]) - a[j]
    print(f'#{i+1} {b}')
'''
# 거꾸로 불러와서 풀기
T = int(input())
for i in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    b = a[-1]
    c = 0
    for j in range(N-1,-1,-1):
        if a[j] > b:
            b = a[j]
        else:
            c += b - a[j]
    print(f'#{i+1} {c}')