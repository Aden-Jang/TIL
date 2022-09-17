N = int(input())
a = list(map(int, input().split()))
rn = int(input())
t = [99] * 50
for i in range(len(a)):
    t[i] = a[i]
t[rn] = 99
q = []
q.append(rn)
while q:
    qp = q.pop(0)
    for i in range(len(t)):
        if t[i] == qp:
            q.append(i)
            t[i] = 99
anslst = []
for i in range(50):
    if t[i] != 99 and i not in t:
        anslst.append(i)
print(len(anslst))
