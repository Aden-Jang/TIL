# def f(arr, x):
#     global g
#     global cnt
#     if not arr:
#         return
#     if arr[(len(arr)-1)//2] == x:
#         cnt += 1
#         return
#     arr1 = arr[0:(len(arr)-1)//2]
#     arr2 = arr[(len(arr)-1)//2+1:len(arr)]
#     if x < arr[(len(arr)-1)//2]:
#         if g == 1:
#             return
#         g = 1
#         f(arr1, x)
#     elif x > arr[(len(arr)-1)//2]:
#         if g == 0:
#             return
#         g = 0
#         f(arr2, x)

def f(s, e, x):
    global cnt
    global g
    while s <= e:
        if a[(s+e)//2] == x:
            cnt += 1
            return
        elif a[(s+e)//2] > x:
            if g == 1:
                return
            g = 1
            e = (s+e)//2 - 1
        elif a[(s+e)//2] < x:
            if g == 0:
                return
            g = 0
            s = (s+e)//2 + 1
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        g = 2
        f(0, N-1, i)
    print(f'#{tc} {cnt}')