T = int(input())
for tc in range(1,T+1):
    P, Pa, Pb = map(int,input().split())
    al = bl = 1
    ar = br = P
    ac = bc = int((1+P)/2)
    ans = 0
    while True:
        if ac < Pa:
            al = ac
        elif ac > Pa:
            ar = ac
        ac = int((al+ar)/2)
        if bc < Pb:
            bl = bc
        elif bc > Pb:
            br = bc
        bc = int((bl + br) / 2)
        if ac == Pa and bc == Pb:
            ans = 0
            break
        elif ac == Pa:
            ans = "A"
            break
        elif bc == Pb:
            ans = "B"
            break
    print(f'#{tc} {ans}')