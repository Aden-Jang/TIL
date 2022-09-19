a, b = map(int, input().split())
minn, maxn = min(a, b), max(a,b)
for i in range(1, minn+1):
    if minn%i == 0:
        if maxn%(minn//i) == 0:
            print(minn//i)
            break
for i in range(1,maxn+1):
    if minn*i % maxn == 0:
        print(minn*i)
        break