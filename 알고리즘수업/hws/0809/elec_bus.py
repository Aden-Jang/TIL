T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    ch = list(map(int,input().split()))
    # 버스의 위치와 충전횟수를 초기화
    bus = 0
    bchange = 0
    # 버스의 위치가 마지막 정류장에 도달할 수 있는 만큼의 위치에 도달할 때 까지 반복
    while bus < N-K:
        for i in range(K,0,-1):
            if bus+i in ch:
                bus += i
                bchange += 1
                break
            elif i == 1:
                bchange = 0
        if bchange == 0:
            break
    print(f'#{tc} {bchange}')


# T = int(input())
# for tc in range(1,T+1):
#     K, N, M = map(int,input().split())
#     ch = list(map(int,input().split()))
#     # 버스의 위치와 충전횟수를 초기화
#     ch.append(N)
#     start = prev = ans = 0
#     for nxt in ch:
#         if nxt-prev > K:
#             ans = 0
#             break
#         if nxt-start > K:
#             start = prev
#             ans += 1
#         prev = nxt
#     print(f'#{tc} {ans}')