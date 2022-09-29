# # quick
# def partition(l, r):
#     pivot = A[l]
#     i, j = l, r
#     while i <= j:
#         while i <= j and A[i] <= pivot:
#             i += 1
#         while i <= j and A[j] >= pivot:
#             j -= 1
#         if i < j:
#             A[i], A[j] = A[j], A[i]
#     A[l], A[j] = A[j], A[l]
#     return j
#
# def qsort(l, r):
#     if l < r:
#         s = partition(l, r)
#         qsort(l, s-1)
#         qsort(s+1, r)
#
# A = [7, 2, 5, 3, 4, 5]
# N = len(A)
# qsort(0, N-1)
# print(A)
#
# 부분집합의 합
def f1(i, k, t):
    global cnt
    cnt += 1
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += A[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, k, t)
        bit[i] = 1
        f1(i+1, k, t)

def f2(i, k, t, s):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s:
        return
    else:
        bit[i] = 0
        f2(i + 1, k, t, s)
        bit[i] = 1
        f2(i + 1, k, t, s+A[i])
    return

def f3(i, k, t, s, rs):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s:
        return
    elif t > s + rs:
        return
    else:
        bit[i] = 0
        f3(i + 1, k, t, s, rs-A[i])
        bit[i] = 1
        f3(i + 1, k, t, s+A[i], rs-A[i])
    return

A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
# f1(0, 10, 10)
# f1(0, 10, 5)
# f1(0, 10, 55)
# f2(0, 10, 10, 0)
# f2(0, 10, 5, 0)
# f2(0, 10, 55, 0)
f3(0, 10, 55, 0, sum(A))
print(cnt)
