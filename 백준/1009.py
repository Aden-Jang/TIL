import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    ans = a
    for i in range(b-1):
        ans = (ans*a)%10

    print(a)