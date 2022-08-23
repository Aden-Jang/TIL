# for tc in range(1, 11):
#     N = int(input())
#     a = list(input())
#     si = []
#     for i in range(N):
#         if a[i] == '*':
#             si.append(i)
#     for i in range(N):
#         if i in si:
#             a[i], a[i + 1] = a[i + 1], a[i]
#     for i in range(N):
#         if a[i] == '+':
#             p = a.pop(i)
#             a.append(p)
#             break
#     stk = []
#     for i in range(N):
#         if a[i].isnumeric():
#             stk.append(int(a[i]))
#         else:
#             p1 = stk.pop()
#             p2 = stk.pop()
#             if a[i] == '*':
#                 p3 = p1 * p2
#             else:
#                 p3 = p1 + p2
#             stk.append(p3)
#     print(f'#{tc} {p3}')


pri = {'+':1, '*':2}
T = 10
for tc in range(1, T+1):
    N = int(input())
    a = input()

    equ = ''
    stk = []
    # [1] 중위표기식 -> 후위표기식
    for i in a:
        if i.isdigit(): # 숫자인 경우: equ에 추가
            equ += i
        else:       # 연산자의 경우
            while stk and pri[i] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(i)
    # 잊지 말고 처리 : 남은 연산자를 순서대로 pop, equ에 추가
    while stk:
        equ += stk.pop()

    # [2] 후위표기식 계산
    for i in equ:
        if i.isdigit():
            stk.append(int(i))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if i == '+':
                stk.append(op1 + op2)
            else:
                stk.append(op1 * op2)

    print(f'#{tc} {stk.pop()}')