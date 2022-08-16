# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     a = list(map(int, input().split()))
#     ans = 0
#     for i in range(N):
#         maxa = a[i]
#         for j in range(i+1, N):
#             if maxa < a[j]:
#                 maxa = a[j]
#         if maxa > a[i]:
#             ans += maxa - a[i]
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    maxa = 0
    for i in range(N-1, -1, -1):
        if maxa < a[i]:
            maxa = a[i]
        ans += maxa - a[i]
    print(f'#{tc} {ans}')