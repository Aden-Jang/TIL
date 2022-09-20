dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
       '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
T = int(input())
for tc in range(1, T + 1):
    N, num = input().split()
    ans = ''
    for i in num:
        d = dic[i]
        for j in range(3, -1, -1):
            if d >= 2 ** j:
                ans += '1'
                d -= 2 ** j
            else:
                ans += '0'
    print(f'#{tc} {ans}')