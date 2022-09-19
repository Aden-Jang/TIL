T = int(input())
dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
dic2 = {'001101':0, '010011':1, '111011':2, '110001':3, '100011':4,
        '110111':5, '001011':6, '111101':7, '011001':8, '101111':9 }
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
    while t[0] == t[-1] == '0':
        if t[0] == t[-1] == '0':
            t = t[1:-1]

    arr = []
    anslst = []
    for i in range(len(t) // 6):
        arr.append(t[6 * i:6 * i + 6])
    for i in arr:
        anslst.append(dic2[i])
    print(f'#{tc}', end=' ')
    print(*anslst)