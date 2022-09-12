import sys

N = int(input())
stack = []
for i in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(int(a[1]))