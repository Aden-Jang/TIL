for _ in range(10):
    tc = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    maxa = 0
    maxa3 = 0
    maxa4 = 0
    for i in range(100): 
        maxa1 = 0
        maxa2 = 0
        maxa3 += a[i][i] # 각 대각선의 합을 구하고 최댓값을 저장
        maxa4 += a[i][99-i]
        for j in range(100):
            maxa1 += a[i][j] # 각 행의 합을 구하고 최댓값을 저장
            maxa2 += a[j][i] # 각 열의 합을 구하고 최댓값을 저장
        maxa = max(maxa, maxa1, maxa2, maxa3, maxa4)
    
    print(f'#{tc} {maxa}')