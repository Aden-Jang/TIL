T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if a[i][4] != a[j][4]:
                if a[i][2] > a[j][2]:
                    maxx = a[i][2]
                else:
                    maxx = a[j][2]
                if a[i][0] < a[j][0]:
                    minx = a[i][0]
                else:
                    minx = a[j][0]
                if a[i][3] > a[j][3]:
                    maxy = a[i][3]
                else:
                    maxy = a[j][3]
                if a[i][1] < a[j][1]:
                    miny = a[i][1]
                else:
                    miny = a[j][1]
                x = maxx-minx-abs(a[i][2]-a[j][2])-abs(a[i][0]-a[j][0])+1
                y = maxy-miny-abs(a[i][3]-a[j][3])-abs(a[i][1]-a[j][1])+1
                if x>0 and y>0:
                    ans += x * y

    print(f'#{tc} {ans}')