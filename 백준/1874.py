from collections import deque

n = int(input())
x = 1
stack = deque()
anslst = deque()
for _ in range(n):
    a = int(input())
    if x > n:
        sp = stack.pop()
        if sp == a:
            anslst.append('-')
        else:
            anslst = 'NO'
            break

    while x <= n:
        if x < a:
            stack.append(x)
            anslst.append('+')
            x += 1

        elif x == a:
            stack.append(x)
            anslst.append('+')
            stack.pop()
            anslst.append('-')
            x += 1
            break

        elif x > a:
            sp = stack.pop()
            if sp == a:
                anslst.append('-')
                break

            else:
                anslst = 'NO'
                break


    if anslst == 'NO':
        break
if anslst == 'NO':
    print(anslst)
else:
    print(*anslst, sep='\n')