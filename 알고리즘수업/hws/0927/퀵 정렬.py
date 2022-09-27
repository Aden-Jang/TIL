def qsort(li):
    if len(li) <= 1:
        return li
    pv = li[0]
    li = li[1:]
    left, right = [i for i in li if i <= pv], [i for i in li if i > pv]
    return qsort(left)+[pv]+qsort(right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    print(f'#{tc} {qsort(a)[N//2]}')
