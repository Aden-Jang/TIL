# T = int(input())
# for tc in range(1, T+1):
#     a = list(input())
#     si = []
#     for i in range(len(a)):
#         if a[i] == '*':
#             si.append(i)
#     for i in range(len(a)):
#         if i in si:
#             a[i], a[i+1] = a[i+1], a[i]
#     for i in range(len(a)):
#         if a[i] == '+':
#             p = a.pop(i)
#             a.append(p)
#             break
#     print(f'#{tc}', end=' ')
#     print(*a, sep='')

pri = {'+':1, '*':2}
T = int(input())
for tc in range(1, T+1):
    a = input()

    equ = ''
    stk = []
    # [1] 중위 표기식 -> 후위표기식
    for i in a:
        if i.isdigit(): # 숫자인 경우: equ에 추가
            equ += i
        else:       # 연산자의 경우
            while stk and pri[i] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(i)
    # [1] 남은 연산자를 순서대로 pop, equ에 추가
    while stk:
        equ += stk.pop()

    print(f'#{tc} {equ}')