import statistics
N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
a.sort()
print(round(sum(a)/N))
print(a[N//2])
print(statistics.mode(a))
print(max(a) - min(a))