a = int(input())
while a != 0:
    a = str(a)
    pa = a[::-1]
    if a == pa:
        print('yes')
    else:
        print('no')
    a = int(input())