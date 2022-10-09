dic = {2:(2, 4, 8, 6), 3:(3, 9, 7, 1), 4:(4, 6), 7:(7, 9, 3, 1), 8:(8, 4, 2, 6), 9:(9, 1)}


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a in [1, 5, 6]:
        print(a)
    elif a in [2, 3, 7, 8]:
        print(dic[a][(b % 4)-1])
    elif a in [4, 9]:
        print(dic[a][(b % 2)-1])
    elif a == 0:
        print(10)