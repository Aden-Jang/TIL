for i in range(1,11):
    e=0
    a = int(input())
    b = list(map(int,input().split()))
    for j in range(2,a-2):
        c = [b[j-2],b[j-1],b[j],b[j+1],b[j+2]]
        if max(c) == c[2]:
            d = c[2]
            c.pop(2)
            e += d - max(c)
    print(f'#{i} {e}')