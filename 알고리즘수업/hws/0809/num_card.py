T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = int(input())
    nums = []
    for i in range(N):
        nums.append(a%10)
        a = a//10
    na = [0] * 10
    for i in nums:
        na[i] += 1
    ans = na[0]
    for i in range(len(na)):
        if na[i] >= ans:
            ans = na[i]
            idx = i
    print(f'#{tc} {idx} {ans}')