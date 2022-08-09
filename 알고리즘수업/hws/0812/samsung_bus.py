T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dica = dict()
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A,B+1):
            if j in dica:
                dica[j] += 1
            else:
                dica[j] = 1
    P = int(input())
    a = []
    for i in range(P):
        a.append(int(input()))
    print(f'#{tc}',end=' ')
    for i in a:
        print(dica[i],end=' ')
    print()