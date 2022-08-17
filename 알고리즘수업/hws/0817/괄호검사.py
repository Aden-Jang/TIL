# T = int(input())
# for tc in range(1, T+1):
#     a = input()
#     ans = 0
#     for i in range(len(a)):
#         if a[i] == '(':
#             ans += 1
#         elif a[i] == ')':
#             ans -= 1
#     if ans == 0:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

T = int(input())
for tc in range(1, T+1):
    a = input()
    stk = []
    ans = 1
    for i in a:
        if i == '(':
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                ans = 0
                break
    if stk:
        ans = 0
    print(f'#{tc} {ans}')