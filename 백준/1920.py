import sys
input = sys.stdin.readline
N = int(input())
a = set(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
for i in num:
    if i in a:
        print(1)
    else:
        print(0)