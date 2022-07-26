def hansoo():
    N = int(input())
    a = 0
    for i in range(1, N+1):
        if i < 100:
            a += 1
        elif i < 1000:
            if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
                a += 1
    return a
print(hansoo())