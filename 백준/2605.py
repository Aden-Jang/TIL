N = int(input())
sor = list(map(int, input().split()))
a = []
for i in range(N):
    a.insert(sor[i],i+1)
a.reverse()
print(*a)