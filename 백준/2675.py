T = int(input())
for j in range(T):
    R, S = input().split()
    R = int(R)
    a=''
    for i in S:
        a += i * R
    print(a)