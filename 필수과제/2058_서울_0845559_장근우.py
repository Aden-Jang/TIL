N=int(input())
l=0
while N>0:
    l+=N%10
    N=N//10
print(l)