def rsp(s, e):
    if a[s] == a[e]:
        return s
    else:
        for i in [s, e]:
            if a[i] == dic[str([a[s], a[e]])]:
                return i

def half(i, j):
    if i == j:
        return i
    fi = half(i, (i+j)//2)
    fj = half((i+j)//2+1, j)
    return rsp(fi, fj)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    dic = {'[1, 3]' : 1, '[3, 1]' : 1, '[1, 2]' : 2, '[2, 1]' : 2, '[2, 3]' : 3, '[3, 2]' : 3}
    print(f'#{tc} {half(0, N-1)+1}')