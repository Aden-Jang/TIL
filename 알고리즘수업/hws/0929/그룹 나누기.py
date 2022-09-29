def find(x):
    if x != lst[x]:
        lst[x] = find(lst[x])
    return lst[x]

def union(x, y):
    global lst
    a = find(x)
    b = find(y)
    if a == b:
        return

    if a > b:
        lst[a] = b
    else:
        lst[b] = a

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    lst = [i for i in range(N+1)]

    for i in range(M):
        union(a[2*i], a[2*i+1])

    ans = 0
    for i in range(1,N+1):
        if lst[i] == i:
            ans += 1
    print(f'#{tc} {ans}')
