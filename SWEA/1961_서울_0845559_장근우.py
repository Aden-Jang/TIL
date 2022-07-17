T=int(input())
for i in range(1,T+1):
    N=int(input())
    h=[]
    for _ in range(N):
        A=list(map(int,input().split()))
        h.append(A)
    a=[]
    for _ in range(N):
        a.append([])

    for p in range(N):
        for o in range(N):
            a[p].append(h[N-o-1][N-p-1])

    for j in range(N):
        for k in range(N):
            a[N-j-1].append(h[N-j-1][N-k-1])

    for q in range(N):
        for r in range(N):
            a[N-q-1].append(h[r][N-q-1])
    cnt=0
    print("#",i,sep='')
    for l in range(N-1,-1,-1):
        for m in range(N*3):
            cnt+=1
            if cnt==N:
                print(a[l][m],end=' ')
                cnt=0
            else:
                print(a[l][m], end='')
        print(' ')