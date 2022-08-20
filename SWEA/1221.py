T = int(input())
for _ in range(T):
    dic = {'ZRO' : 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0}
    tc, la = input().split()
    a = list(input().split())
    for i in a:
        dic[i] += 1
    print(tc)
    for i in dic:
        for j in range(dic[i]):
            print(i, end=' ')
    print()