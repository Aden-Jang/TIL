T = int(input())
for i in range(T):
    a = input()
    b = 0
    for j in range(len(a)-1):
        if (a[j:j+2] == '(|') or (a[j:j+2] == '|)') or (a[j:j+2] == '()'):
            b += 1
    print(f'#{i+1} {b}')
