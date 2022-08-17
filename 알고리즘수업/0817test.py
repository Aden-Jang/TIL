# stack1_stack
stackSize = 10
stack = [0] * stackSize
top = -1

top += 1        # push(1) 탑 증가
stack[top] = 1  # 스택에 push

top += 1        # push(2)
stack[top] = 2

top -= 1
temp = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1
print(temp)

stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())

# stack1_재귀
def f(i, N):        # i 현재 단계, N 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)
# f(0, 1000) -> 재귀 호출 횟수 초과 오류 - 재귀의 횟수는 엄청 많다면(수백번) 접근방식이 틀린것

# stack1_재귀
# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i, N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있는 경우
        print(A[i])
        B[i] = A[i]
        f(i+1, N)   # 다음 원소로 이동
N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)

# stack1_recur  -> pypy를 돌리면 가능
# def f(i, N):        # i 현재 단계, N 목표 단계
#     if i == N:
#         print(i)
#         return
#     else:
#         print(i)
#         f(i+1, N)
#
# f(0, 1000)

# stack1_facto
def f(n):       # 팩토리얼 n! 1! = 1
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))

# stack1_fibo
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))