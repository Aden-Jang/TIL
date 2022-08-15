T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    ans = len(A)
    p = []
    for i in range(len(A)-len(B)+1):
        if i in p:
            continue
        if A[i:i+len(B)] == B:
            ans -= len(B) - 1
            for j in range(i, i+len(B)):
                p.append(j)
    print(f'#{tc} {ans}')