dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
       '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }
C = int(input())
for tc in range(1, C+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in arr:
        if '1' in i:
            a = i
            break
    for i in range(len(a)-1,-1,-1):
        if a[i] == '1':
            a = a[i-55:i+1]
            break
    ans = []
    anslst = []
    for i in range(len(a) // 7):
        ans.append(a[7 * i:7 * i + 7])
    for i in ans:
        anslst.append(dic[i])
    x = 0
    sx = 0
    for i in range(8):
        if i % 2 == 0:
            x += anslst[i]
        else:
            sx += anslst[i]
    sx += 3*x
    if sx % 10 == 0:
        print(f'#{tc} {sum(anslst)}')
    else:
        print(f'#{tc} {0}')