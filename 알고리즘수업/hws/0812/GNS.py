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
        for j in cnt:
            f += [numbers[i]] * j
    print(f'#{tc} {f}')