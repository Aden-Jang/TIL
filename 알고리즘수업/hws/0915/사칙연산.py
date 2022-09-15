def posto(n):
    global st
    if n:
        posto(ch1[n])
        posto(ch2[n])
        st.append(t[n])

for tc in range(1, 11):
    N = int(input())
    t = [0] * (N+1)
    a = [list(input().split()) for _ in range(N)]
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for i in range(N):
        if a[i][1].isnumeric():
            t[i+1] = int(a[i][1])
        else:
            t[i+1] = a[i][1]
            if len(a[i]) == 4:
                ch1[i+1] = int(a[i][2])
                ch2[i+1] = int(a[i][3])
    st = []
    posto(1)

    lst = []
    while st:
        p = st.pop(0)
        if type(p) == type(1):
            lst.append(p)
        else:
            a2 = lst.pop()
            a1 = lst.pop()
            if p == '-':
                lst.append(a1 - a2)
            if p == '+':
                lst.append(a1 + a2)
            if p == '*':
                lst.append(a1 * a2)
            if p == '/':
                lst.append(a1 / a2)
    print(f'#{tc} {int(lst[0])}')

