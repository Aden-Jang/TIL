T = int(input())
dic = {'0': '0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
       '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
       'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

dic2 = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4, '1231': 5,
        '1114': 6, '1312': 7, '1213': 8, '3112': 9, }

def b(a, nn):
    cnt0 = 0
    cnt1 = 0
    qwer = ''
    for i in a:
        if i == '0':
            cnt0 += 1
            if cnt1 != 0:
                qwer += qwer + str(cnt1//nn)
                cnt1 = 0
        else:
            cnt1 += 1
            if cnt0 != 0:
                qwer += qwer + str(cnt0//nn)
                cnt0 = 0
    zxcv = ''
    print(qwer)
    for i in range(0, len(qwer), 4):
        zxcv += str(dic2[qwer[i:i+4]])

    return zxcv


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = [input().strip() for _ in range(N)]
    ma = M
    for i in a:
        if i.count('0') < ma:
            ma = i.count('0')
            aa = i

    ansa = ''
    for i in aa:
        ansa += dic[i]
    ans = ansa.split()
    for i in range(len(ans)):
        ans[i] = '0000' + ans[i].rstrip('0')
        for j in range(len(ans[i])-1, -1, -1):
            if ans[i][j] == '1':
                nn = len(ans[i])//56
                ans[i] = ans[i][j-(56*nn-1):j+1]
                break
    print(ans)
    # for i in ans:
    #     # num = b(i, nn)
    #     # if num
    #     print(i)