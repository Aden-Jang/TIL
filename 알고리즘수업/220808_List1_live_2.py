T = int(input())
for tc in range(T):
    numli = list(map(int,input()))
    a = [0] * 12
    triplet = 0
    run1 = 0
    for i in numli:
        a[i] += 1
    print(a)
    i=0
    while i <= 9:
        if a[i] >= 3:
            a[i] -= 3
            triplet += 1
            print(a)
            continue
        elif a[i] >= 1 and a[i+1] >= 1 and a[i+2] >= 1:
            a[i] -=1
            a[i+1] -=1
            a[i+2] -=1
            print(a)
            run1 += 1
            continue
        i+=1
    if triplet + run1 == 2:
        print(f"#{tc+1} 1")
    else:
        print(f"#{tc+1} 0")
