T = int(input())
for tc in range(1, T+1):
    a = input()
    op = 0
    st = 0
    for i in range(len(a)-1):
        if a[i:i+2] == '()':
            st += op
        elif i != 0 and a[i-1:i+1] == '()':
            continue
        elif a[i] == '(':
            op += 1
            st += 1
        else:
            op -= 1
    print(f'#{tc} {st}')