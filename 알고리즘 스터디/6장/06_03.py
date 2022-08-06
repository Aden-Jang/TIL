logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
a = []
b = []
for i in logs:
    if i[0:3] == 'dig':
        a.append(i)
    else:
        b.append(i)
print(a)
b.sort()
print(b)