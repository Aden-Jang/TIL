T=int(input())
for i in range(1,T+1):
    s=[]
    stop=0
    for _ in range(9):
        A = list(map(int, input().split()))
        s.append(A)
    for j in range(9):
        a=[1,2,3,4,5,6,7,8,9]
        for k in range(9):
            if s[j][k] in a:
                a.remove(s[j][k])
            else:
                print("#",i," 0",sep="")
                stop=1
                break
        if stop==1:
            break
    if stop == 1:
        continue
    else:
        for l in range(9):
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for m in range(9):
                if s[m][l] in a:
                    a.remove(s[m][l])
                else:
                    print("#",i," 0",sep="")
                    stop = 1
                    break
            if stop==1:
                break
    if stop == 1:
        continue
    else:
        for n in range(3):
            for o in range(3):
                a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for p in range(3):
                    for q in range(3):
                        if s[n*3+p][o*3+q] in a:
                            a.remove(s[n*3+p][o*3+q])
                        else:
                            print("#",i," 0",sep="")
                            stop = 1
                            break
                    if stop == 1:
                        break
                if stop == 1:
                    break
            if stop == 1:
                break
    if stop == 0:
        print("#",i," 1",sep="")