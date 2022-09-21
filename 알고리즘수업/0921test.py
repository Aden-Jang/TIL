# # npr1
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         if i != j:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     print(i, j, k)
#
# # npr2
# def f(i, k):
#     if i == k:          # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# p = [1, 2, 3]
# f(0, 3)
#
# p = [1, 2, 3, 4, 5]
# f(0, 5)
#
# # npr3
# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k)           # p[i+1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 3
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * N
# f(0,N)

# # npr3-2 (기본형)
# def f(i, k, r):
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k, r)           # p[i+1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 5
# R = 3
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * R
# f(0, N, R)
#
# # npr3-3 (베이비진 풀이)
# def f(i, k, r):
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k, r)           # p[i+1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 6
# R = 6
# a = [1, 2, 4, 7, 8, 3]
# used = [0] * N
# p = [0] * R
# f(0, N, R)
#
# # npr3-4
# def f(i, k, r):
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k, r)           # p[i+1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 5
# R = 5
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * R
# # p[0] = 1
# # used[0] = 1
# # f(1, N, R)
# p[0] = 2
# used[1] = 1
# f(1, N, R)

#
# # 배열의 합
# def f(i, k):
#     global minV
#     if i == k:
#         s = 0           # 모든 j행에서 p[j]열을 골랐을 때의 합
#         for j in range(k):
#             s += arr[j][p[j]]
#         if minV > s:
#             minV = s
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [i for i in range(N)]            # p[i] i행에서 선택한 열 번호
#     minV = N * 10
#     f(0, N)
#     print(f'#{tc} {minV}')
#
# # 배열의 합2
# def f(i, k, s):
#     global cnt
#     global minV
#     cnt += 1
#     if i == k:          # 인덱스 i == 원소의 개수
#         if minV > s:
#             minV = s
#     elif s >= minV:
#         return
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k, s + arr[i][p[i]])
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [i for i in range(N)]            # p[i] i행에서 선택한 열 번호
#     minV = N * 10
#     cnt = 0
#     f(0, N, 0)
#     print(f'#{tc} {minV} {cnt}')

#
# # 부분집합
#
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1, 1<<n):
#     for j in range(n):
#         if i & (1<<j):      # j번 비트가 0이 아니면 arr[j] 부분집합의 원소
#             print(arr[j], end = ' ')
#     print()
#
# # 부분집합 재귀
#
# def f(i, k):
#     if i == k:
#         # print(bit)
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end=' ')
#         print()
#     else:
#         bit[i] = 0
#         f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# bit = [0] * n       # bit[i] arr[i]가 부분집합의 원소인지 표시
# f(0, n)
#
# # 조합1
#
# N = 10
# for i in range(N - 2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i, j, k)
#
# # 조합2
#
# def nCr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             nCr(n, r-1, i+1)
#
# A = [1, 2, 3, 4, 5]
# n = len(A)
# r = 3
# comb = [0] * r
# nCr(n, r, 0)
#
# # babygin1
# '''
# 5
# 123123
# 124467
# 333444
# 444456
# 123444
# '''
#
# def f(i, k):
#     global ans
#     if i == k:
#         run = 0
#         tri = 0
#         if card[0] == card[1] and card[1] == card[2]:
#             tri += 1
#         if card[0]+1 == card[1] and card[1]+1 == card[2]:
#             run += 1
#         if card[3] == card[4] and card[4] == card[5]:
#             tri += 1
#         if card[3]+1 == card[4] and card[4]+1 == card[5]:
#             run += 1
#         if tri+run == 2:
#             return 1
#         else:
#             return 0
#     else:
#         for j in range(i, k):
#             card[i], card[j] = card[j], card[i]
#             if f(i+1, k):
#                 return 1
#             card[i], card[j] = card[j], card[i]
#         return 0
# T = int(input())
# for tc in range(1, T + 1):
#     card = list(map(int, input()))
#     ans = f(0, 6)
#     if ans:
#         print(f'#{tc} Baby Gin')
#     else:
#         print(f'#{tc} Lose')
#
# babygin2
'''
5
123123
124467
333444
444456
123444
'''

T = int(input())
for tc in range(1, T + 1):
    card = int(input())
    c = [0] * 12

    i = 0
    while i < 6:
        c[card%10] += 1
        card //= 10
        i += 1
    tri = 0
    run = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')