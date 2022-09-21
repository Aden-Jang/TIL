N = int(input())
a = list(map(int, input().split()))
dic = dict()
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
M = int(input())
ma = list(map(int, input().split()))

for i in ma:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
