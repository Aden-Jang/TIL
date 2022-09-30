T = int(input())
for tc in range(1, T+1):
    d, m, tm, y = map(int, input().split())
    a = list(map(int, input().split()))
    answer = y
    da = []
    ma = [m]*12
    ans = [0] * 12
    for i in a:
        da.append(i*d)
    for i in range(12):
        ans[i] = min(da[i], ma[i])
    answer = min(sum(ans), answer)
    for i in range(12):
        for k in range(12):
            ans[k] = min(da[k], ma[k])
        j = i
        while j <= 12:
            if sum(ans[j:j+3]) > tm:
                ans[j] = tm
                if j < 10:
                    ans[j+1] = ans[j+2] = 0
                elif j == 10:
                    ans[j+1] = 0
                answer = min(sum(ans), answer)
            j += 3
    print(f'#{tc} {answer}')