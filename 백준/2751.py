import sys
input = sys.stdin.readline
N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
a.sort()
print(*a, sep='\n')