T = int(input())
for _ in range(T):
    dic = {'ZRO' : 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0}
    tc, la = input().split()
    a = list(input().split())
    for i in a:
        dic[i] += 1
    print(tc)
    for i in dic:
        for j in range(dic[i]):
            print(i, end=' ')
    print()

T = int(input())
for tc in range(1, T+1):
    q, N = map(str, input().split())
    N = int(N)
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = list(map(str, input().split()))
    for i in range(N):
        for j in range(len(numbers)):
            if numbers[j] == a[i]:
                cnt[j] += 1
                break
    f = []
    for i in range(10):
        f += [numbers[i]] * cnt[i]
    print(f'#{tc}')
    print(*f)