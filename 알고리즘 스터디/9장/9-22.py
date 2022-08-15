temperatures = [15, 16, 12, 13, 18]
ans = []
for i in range(len(temperatures)-1):
    ansx = 1
    for j in range(i+1, len(temperatures)):
        if j == len(temperatures) - 1 and temperatures[i] >= temperatures[j]:
            ansx = 0
            break
        elif temperatures[i] < temperatures[j]:
            break
        else:
            ansx += 1
    ans.append(ansx)
ans.append(0)
print(ans)