w = input()
w = w.upper()
a = [0] * 26
for i in w:
    a[ord(i)-ord('A')] += 1
if max(a) in a[a.index(max(a))+1:]:
    print('?')
else:
    print(chr(a.index(max(a))+ord('A')))