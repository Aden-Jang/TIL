# # tree1
#
# '''
# 정점 번호 V = 1~(E+1)
# 간선 수
# 부모-자식 순
# 4
# 1 2 1 3 3 4 3 5
# '''
# def preo(n):         # 전위 순회
#     if n:
#         print(n)    # visit(n)
#         preo(ch1[n])
#         preo(ch2[n])
#
# def ino(n):         # 중위 순회
#     if n:
#         ino(ch1[n])
#         print(n)    # visit(n)
#         ino(ch2[n])
#
# def posto(n):         # 후위 순회
#     if n:
#         posto(ch1[n])
#         posto(ch2[n])
#         print(n)    # visit(n)
#
# E = int(input())
# a = list(map(int, input().split()))
# V = E + 1
# root = 1
# # 부모를 인덱스로 자식 번호 저장
# ch1 = [0] * (V + 1)
# ch2 = [0] * (V + 1)
# # for j in range(0, E*2, 2):
# #     p, c = a[j], a[j+1]
# for i in range(E):
#     p, c = a[i*2], a[i*2+1]
#     if ch1[p] == 0:     # 아직 자식이 없으면
#         ch1[p] = c      # 자식1로 저장
#     else:
#         ch2[p] = c
# print(ch1, ch2)
#
# preo(root)
# print()
# ino(root)
# print()
# posto(root)
#
#
# # tree2
# '''
# 정점 번호 V = 1~(E+1)
# 간선 수
# 부모-자식 순
# 4
# 1 2 1 3 3 4 3 5
# '''
# def find_root(V):
#     for i in range(1, V + 1):
#         if par[i] == 0:  # 부모가 없으면 root
#             return i
#
# E = int(input())
# a = list(map(int, input().split()))
# V = E + 1
#
# ch1 = [0] * (V + 1)
# ch2 = [0] * (V + 1)
# # 자식을 인덱스로 부모 번호 저장
# par = [0] * (V + 1)
# for i in range(E):
#     p, c = a[i*2], a[i*2+1]
#     if ch1[p] == 0:     # 아직 자식이 없으면
#         ch1[p] = c      # 자식1로 저장
#     else:
#         ch2[p] = c
#     par[c] = p
# root = find_root(V)
# print(root)
#
#
# # tree3
#
# def preo(n):
#     if n <= size:
#         print(tree[n])
#         preo(2*n)
#         preo(2*n+1)
#
# tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']    # 완전이진트리
# size = len(tree) - 1
# preo(1)
# preo(2)
#
# # tree연습문제
# '''
# 정점 번호 V = 1~(E+1)
# 간선 수
# 부모-자식 순
# 4
# 1 2 1 3 3 4 3 5
# '''
# def find_root(V):
#     for i in range(1, V + 1):
#         if par[i] == 0:  # 부모가 없으면 root
#             return i
#
# def preo(n):         # 전위 순회
#     # global cnt
#     if n:
#         # cnt += 1  # 간선의 개수
#         # cnt = n   # 마지막으로 나오는 숫자
#         print(n, end = ' ')    # visit(n)
#         preo(ch1[n])
#         preo(ch2[n])
#
# def ino(n):         # 중위 순회
#     if n:
#         ino(ch1[n])
#         print(n, end = ' ')    # visit(n)
#         ino(ch2[n])
#
# def posto(n):         # 후위 순회
#     if n:
#         posto(ch1[n])
#         posto(ch2[n])
#         print(n, end = ' ')    # visit(n)
#
# V = int(input())
# a = list(map(int, input().split()))
# E = V - 1
#
# ch1 = [0] * (V + 1)
# ch2 = [0] * (V + 1)
# par = [0] * (V + 1)
# for i in range(E):
#     p, c = a[i*2], a[i*2+1]
#     if ch1[p] == 0:
#         ch1[p] = c
#     else:
#         ch2[p] = c
#     par[c] = p
# root = find_root(V)
# # cnt = 0
# preo(root)
# print()
# ino(root)
# print()
# posto(root)
#
# # tree연습문제2
# '''
# 정점 번호 V = 1~(E+1)
# 간선 수
# 부모-자식 순
# 4
# 1 2 1 3 3 4 3 5
# '''
# def find_root(V):
#     for i in range(1, V + 1):
#         if par[i] == 0:  # 부모가 없으면 root
#             return i
#
# def preo(n):         # 전위 순회
#     # global cnt
#     if n:
#         # cnt += 1  # 간선의 개수
#         # cnt = n   # 마지막으로 나오는 숫자
#         print(n, end = ' ')    # visit(n)
#         preo(ch1[n])
#         preo(ch2[n])
#
# def ino(n):         # 중위 순회
#     if n:
#         ino(ch1[n])
#         print(n, end = ' ')    # visit(n)
#         ino(ch2[n])
#
# def posto(n):         # 후위 순회
#     if n:
#         posto(ch1[n])
#         posto(ch2[n])
#         print(n, end = ' ')    # visit(n)
#
# def f(n):           # global cnt 없이 순회한 정점 수를 리턴하는 함수
#     if n == 0:      # 서브트리가 비어있으면
#         return 0
#     else:
#         L = f(ch1[n])
#         R = f(ch2[n])
#         return L + R + 1
#
# E = int(input())
# a = list(map(int, input().split()))
# V = E + 1
#
# ch1 = [0] * (V + 1)
# ch2 = [0] * (V + 1)
# par = [0] * (V + 1)
# for i in range(E):
#     p, c = a[i*2], a[i*2+1]
#     if ch1[p] == 0:
#         ch1[p] = c
#     else:
#         ch2[p] = c
#     par[c] = p
# root = find_root(V)
# print(f(root))
# # # cnt = 0
# # preo(root)
# # print()
# # ino(root)
# # print()
# # posto(root)

# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    c = last
    p = c //2       # 완전 이진 트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식 인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c+1]:    # 오른쪽 자식이 있고, 오른쪽 자식이 더 크면
            c += 1          # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대 힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c           # 자식을 새로운 부모로
            c = p * 2       # 왼쪽 자식 번호를 계산
        else:               # 부모가 더 크면
            break           # 비교 중단,
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
# print(heap)

while last:
    print(deq())