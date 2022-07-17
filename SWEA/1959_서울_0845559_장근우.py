T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())

    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for l in range(abs(N-M)+1):
        if N>M:
            C=[]
            for l in range(abs(N-M)+1):
                k=0
                num=0
                for j in range(M):
                    num+=A[l]*B[k]
                    k+=1
                    l+=1
                C.append(num)
        elif N==M:
            C = []
            k = 0
            num = 0
            for j in range(N):
                num += A[k] * B[k]
                k += 1
            C.append(num)
        else:
            C = []
            for l in range(abs(N-M)+1):
                k = 0
                num = 0
                for j in range(N):
                    num += A[k] * B[l]
                    k += 1
                    l += 1
                C.append(num)
    print("#", i, sep='', end=' ')
    print(max(C))
