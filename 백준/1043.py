N, M = map(int, input().split())
k = list(map(int, input().split()))
kn = k.pop(0)
pnlst = []
plst = []
pklst = [1] * M
for i in range(M):
    p = list(map(int, input().split()))
    pn = p.pop(0)
    pnlst.append(pn)
    plst.append(p)
m = 0
while kn != m:
    m = kn
    for i in range(M):
        for j in range(kn):
            if k[j] in plst[i]:
                pklst[i] = 0
                for l in plst[i]:
                    k.append(l)
        k = list(set(k))
        kn = len(k)
print(sum(pklst))