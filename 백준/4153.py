import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
while not a == b == c == 0:
    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2
    if a2 + b2 + c2 - (max(a2, b2, c2)) == max(a2, b2, c2):
        print("right")
    else:
        print("wrong")
    a, b, c = map(int, input().split())