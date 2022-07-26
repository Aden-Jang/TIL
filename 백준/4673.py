def d():
    a = []
    for i in range(10000):
        if i < 10:
            a.append(i + i)
        elif i < 100:
            a.append(i + int(str(i)[0]) + int(str(i)[1]))
        elif i < 1000:
            a.append(i + int(str(i)[0]) +int(str(i)[1]) +int(str(i)[2]))
        elif i < 10000:
            a.append(i + int(str(i)[0]) +int(str(i)[1]) +int(str(i)[2]) +int(str(i)[3]))
    b = list(range(1,10000,1))
    for j in a:
        if j in b:
            b.remove(j)
    for k in b:
        print(k)
d()