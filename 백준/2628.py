w, h = map(int, input().split())
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
hlst = [0, h]
wlst = [0, w]

for i in range(N):
    if a[i][0] == 0:
        hlst.append(a[i][1])
    else:
        wlst.append(a[i][1])
hlst.sort()
wlst.sort()
mh = []
mw = []
for i in range(len(hlst) - 1):
    mh.append(hlst[i+1] - hlst[i])
for i in range(len(wlst) - 1):
    mw.append(wlst[i + 1] - wlst[i])
print(max(mh) * max(mw))