N = int(input())
arr = [[] for _ in range(51)]
a = [input() for _ in range(N)]
for i in range(N):
    arr[len(a[i])].append(a[i])
for i in range(51):
    if arr[i]:
        arr[i] = list(set(arr[i]))
        arr[i].sort()
for i in range(1, 51):
    if arr[i]:
        print(*arr[i], sep='\n', end='\n')