di1 = [0, 1, 0, -1]     # + 모양
dj1 = [1, 0, -1, 0]
di2 = [1, 1, -1, -1]    # x 모양
dj2 = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]             # i, j를 중심으로 + 모양
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i + di1[k] * z, j + dj1[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt1 += arr[ni][nj]
            if maxV < cnt1:
                maxV = cnt1
            cnt2 = arr[i][j]
            for di, dj in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                for z in range(1, M):
                    ni, nj = i + di * z, j + dj * z
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt2 += arr[ni][nj]
            if maxV < cnt2:
                maxV = cnt2

    print(f'#{tc} {maxV}')