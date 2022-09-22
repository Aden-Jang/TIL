T = int(input())
for tc in range(1, T + 1):
    a = list(map(int, input().split()))
    A = []
    B = []
    ans = 0
    for i in range(len(a)):
        if ans:
            break
        if i % 2 == 0:
            A.append(a[i])
            if len(A) >= 3:
                A.sort()
                for j in range(0, len(A)-2):
                    if A[j] == A[j+1] == A[j+2] or A[j]+2 == A[j+1]+1 == A[j+2]:
                        ans = 1
                        break

            if len(A) >= 4:
                for j in range(0, len(A)-3):
                    if A[j]+2 == A[j+1]+1 == A[j+3]:
                        ans = 1
                        break
        else:
            B.append(a[i])
            if len(B) >= 3:
                B.sort()
                for j in range(0, len(B)-2):
                    if B[j] == B[j+1] == B[j+2] or B[j]+2 == B[j+1]+1 == B[j+2]:
                        ans = 2
                        break
            if len(B) >= 4:
                for j in range(0, len(B) - 3):
                    if B[j]+2 == B[j+1]+1 == B[j+3]:
                        ans = 2
                        break
    print(f'#{tc} {ans}')