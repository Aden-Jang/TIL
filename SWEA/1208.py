for tc in range(1, 11):
    N = int(input())
    a = list(map(int,input().split()))
    for i in range(N):
        if max(a) - min(a) <= 1: # 최대와 최소의 간격이 1이면 멈춤
            break
        else: # 평탄화 작업
            a[a.index(max(a))] -= 1
            a[a.index(min(a))] += 1
    print(f'#{tc} {max(a)-min(a)}')