S = input()
a = []
for i in range(97,123,1):
    if chr(i) in S:
        a.append(str(S.index(chr(i))))
    else:
        a.append('-1')
b = ' '.join(a)
print(b)