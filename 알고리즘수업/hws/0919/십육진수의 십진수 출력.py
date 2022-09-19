T = int(input())
dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
for tc in range(1, T+1):
    a = input()
    t = ''
    for i in a:
        d = dic[i]
        for j in range(3, -1, -1):
            if d >= 2**j:
                t += '1'
                d -= 2**j
            else:
                t += '0'

    arr = []
    anslst = []
    l = len(t)//7
    for i in range(l):
        arr.append(t[7*i:7*i+7])
    if len(t) % 7 != 0:
        arr.append(t[7*(l):])
    for i in arr:
        ans = 0
        for j in range(len(i)):
            if i[j] == '1':
                ans += 2 ** (len(i)-1-j)
        anslst.append(ans)
    print(f'#{tc}',end=' ')
    print(*anslst)