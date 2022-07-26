T = int(input())
for i in range(T):
    a = map(int,input().split())
    print(f'#{i+1} {int(round(sum(a)/10,0))}')