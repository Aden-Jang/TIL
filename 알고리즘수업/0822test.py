# stack2_부분집합

def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        s = 0               # 부분집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        #         print(A[i], end = ' ')
        # print()
        if s == 10:
            answer += 1     # 부분집합의 합이 10인 경우의 수
    else:
        bit[i] = 1 # A[i]가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        
def f2(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        s = 0               # 부분집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        #         print(A[i], end = ' ')
        # print()
        if s == 10:
            answer += 1     # 부분집합의 합이 10인 경우의 수
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ') # 부분집합의 합이 10인 모든 부분집합 프린트
            print()
    else:
        bit[i] = 1 # A[i]가 부분집합에 포함
        f2(i+1, N)
        bit[i] = 0
        f2(i+1, N)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer, cnt)
answer = 0
cnt = 0
f2(0, 10)
print(answer, cnt)



# stack2_부분집합2

def f3(i, N, s, t): # 이전까지의 합을 구해서 다음 값을 더했을 때 넘어가면 그 이후는 생략
    global answer
    global cnt
    cnt += 1
    if i == N:            # 모든 원소가 고려된 경우
        if s == t:              # 부분집합의 합이 t면
            answer += 1
        return
    else:
        f3(i+1, N, s+A[i], t)
        f3(i+1, N, s, t)
        
def f4(i, N, s, t): # 이전까지의 합을 구해서 다음 값을 더했을 때 넘어가면 그 이후는 생략
    global answer
    global cnt
    cnt += 1
    if i == N:              # 모든 원소가 고려된 경우
        if s == t:          # 부분집합의 합이 t면
            answer += 1
        return
    elif s > t:             # 찾는 합 값이 작으면 효과가 좋지만 크면 효과가 적음
        return
    else:
        f4(i+1, N, s+A[i], t)
        f4(i+1, N, s, t)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
cnt = 0
f3(0, 10, 0, 10)
print(answer, cnt)
answer = 0
cnt = 0
f4(0, 10, 0, 10)
print(answer, cnt)
answer = 0
cnt = 0
f4(0, 10, 0, 4)
print(answer, cnt)
answer = 0
cnt = 0
f4(0, 10, 0, 55)
print(answer, cnt)



# stack2_순열1

def f(i, N):
    if i == N:                  # 순열 완성
        print(P)
    else:
        for j in range(i, N):   # p[i]에 들어갈 숫자 p[j]결정
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]


P = [1, 2, 3]
f(0, 3)