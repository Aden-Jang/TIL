dic = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
dic2 = {1:2, 2:1, 3:4, 4:3}

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(K)]
    se = [[[]] * N for _ in range(N)]
    for i in a:
        h, w, num, d = i
        se[h][w] = (num, d)
    for _ in range(M):
        for i in range(N):
            for j in range(N):
                if se[i][j]:
                    p = se[i][j].pop(0)
                    se[i+dic[se[i][j][1]][0]][j+dic[se[i][j][1]][1]].append(p)
                    if i+dic[se[i][j][1]][0]==0 or i+dic[se[i][j][1]][0] == N-1 or j+dic[se[i][j][1]][1] == 0 or j+dic[se[i][j][1]][1]] == N-1:
                        se[i+dic[p[1][1]]][1] = dic2[]

# def move():
#     global M, ans
#     arr.sort(key=lambda x: -x[2])
#     position = []
#     direction = []
#     for i in range(K):
#         # M이 0이면 시간 종료
#         if M == 0:
#             for j in range(N):
#                 ans += sum(visited[j])
#             return
#         if arr[i][2] == 0:
#             continue
#         #이동
#         if arr[i][3] == 1:
#             visited[arr[i][0]][arr[i][1]] -= arr[i][2]
#             arr[i][0] -= 1
#             visited[arr[i][0]][arr[i][1]] += arr[i][2]
#         elif arr[i][3] == 2:
#             visited[arr[i][0]][arr[i][1]] -= arr[i][2]
#             arr[i][0] += 1
#             visited[arr[i][0]][arr[i][1]] += arr[i][2]
#         elif arr[i][3] == 3:
#             visited[arr[i][0]][arr[i][1]] -= arr[i][2]
#             arr[i][1] -= 1
#             visited[arr[i][0]][arr[i][1]] += arr[i][2]
#         elif arr[i][3] == 4:
#             visited[arr[i][0]][arr[i][1]] -= arr[i][2]
#             arr[i][1] += 1
#             visited[arr[i][0]][arr[i][1]] += arr[i][2]
#
#         # 약품이 칠해진 셀에 도착하면 미생물수 절반, 이동방향 반대
#         if arr[i][0] == 0 or arr[i][1] == 0 or arr[i][0] == N-1 or arr[i][1] == N-1:
#             arr[i][2] //= 2
#             if arr[i][3] % 2 == 0:
#                 arr[i][3] -= 1
#             else:
#                 arr[i][3] += 1
#             if arr[i][2] % 2 == 0:
#                 visited[arr[i][0]][arr[i][1]] -= arr[i][2]
#             else:
#                 visited[arr[i][0]][arr[i][1]] -= arr[i][2] + 1
#
#
#         # 미생물이 만나면 군집이 합쳐지고, 미생물 수가 많은 방향으로 통일일
#
#         if [arr[i][0], arr[i][1]] not in position:
#             position.append([arr[i][0], arr[i][1]])
#             direction.append([arr[i][3]])
#         else:
#             arr[i][3] = direction[position.index([arr[i][0], arr[i][1]])][0]
#             for x in range(K):
#                 if arr[x][0] == arr[i][0] and arr[x][1] == arr[i][1]:
#                     arr[x][2] += arr[i][2]
#                     arr[i][2] = 0
#                     break
#     M -= 1
#     move()
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(K)]
#     visited = [[0] * N for _ in range(N)]
#     for k in range(K):
#         visited[arr[k][0]][arr[k][1]] = arr[k][2]
#
#     ans = 0
#
#     move()
#     print(f"#{tc} {ans}")