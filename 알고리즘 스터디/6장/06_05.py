s = ['eat','tea','tan','ate','nat','bat']
'''
# 타임오버
a = []
for i in s:
    if sorted(i) not in a:
        a.append(sorted(i))
b = [[] for _ in range(len(a))]
for i in range(len(s)):
    for j in range(len(a)):
        if sorted(s[i]) == a[j]:
            b[j].append(s[i])
print(b)
'''

l = []
for idx, a in enumerate(s):
    a = ''.join(sorted(a))
    l.append((idx, a))
l=sorted(l, key = lambda x : x[1] )

ans = dict()
print(l)
for i in range(len(l)):
    ans[l[i][1]] = ans.get(l[i][1],[]) + s[l[i][0]]

print(list(ans.values()))