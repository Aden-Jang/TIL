pri = {'+':1, '*':2, '(':0}

for tc in range(1, 11):
    N = int(input())
    a = list(input())

    equ = ''
    stk = []
    # [1] 중위표기식 -> 후위표기식
    for i in a:
        if i.isdigit(): # 숫자인 경우: equ에 추가
            equ += i
        else:       # 연산자의 경우
            if i == ')':
                while stk[-1] != '(':
                    equ += stk.pop()
                stk.pop()
                continue
            elif i == '(':
                stk.append(i)
                continue
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