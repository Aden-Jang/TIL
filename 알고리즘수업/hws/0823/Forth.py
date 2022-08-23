T = int(input())
for tc in range(1, T+1):
    a = list(input().split())
    stk = []
    i = 0
    ans = 0
    while a[i] != '.':
        if a[i].isdigit():
            stk.append(int(a[i]))

        else:
            if len(stk) < 2:
                ans = 'error'
                break
            else:
                op2 = stk.pop()
                op1 = stk.pop()
                if a[i] == '+':
                    stk.append(op1 + op2)
                elif a[i] == '-':
                    stk.append(op1 - op2)
                elif a[i] == '*':
                    stk.append(op1 * op2)
                elif a[i] == '/':
                    stk.append(op1 // op2)
        i += 1
    if len(stk) != 1:
        ans = 'error'
    if ans != 'error':
        ans = stk.pop()
    print(f'#{tc} {ans}')
