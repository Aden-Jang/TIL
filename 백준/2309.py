n = []
for _ in range(9):
    n.append(int(input()))
sm = sum(n)
for i in range(9):
    for j in range(i+1, 9):
        if sm - n[i] - n[j] == 100:
            n.pop(j)
            n.pop(i)
            break
    if len(n) == 7:
        break
n.sort()
print(*n, sep='\n')
