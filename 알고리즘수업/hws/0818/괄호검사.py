T = int(input())
for tc in range(1, T+1):
    a = input()
    i = 0
    stack = []
    ans = 1
    while i <= len(a)-1:
        if a[i] == "(":
            stack.append(a[i])
        elif a[i] == "{":
            stack.append(a[i])
        elif a[i] == "[":
            stack.append(a[i])
        elif a[i] == ")":
            if stack != []:
                b = stack.pop()
            else:
                ans = 0
                break
            if b == "(":
                pass
            else:
                ans = 0
                break
        elif a[i] == "}":
            if stack != []:
                b = stack.pop()
            else:
                ans = 0
                break
            if b == "{":
                pass
            else:
                ans = 0
                break
        elif a[i] == "]":
            if stack != []:
                b = stack.pop()
            else:
                ans = 0
                break
            if b == "[":
                pass
            else:
                ans = 0
                break
        else:
            pass
        i += 1
    if stack != []:
        ans = 0
    print(f'#{tc} {ans}')