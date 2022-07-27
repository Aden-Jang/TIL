A, B = input().split()
A = int(''.join(reversed(A)))
B = int(''.join(reversed(B)))
print(max(A, B))