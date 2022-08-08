# Baby-gin Game
'''
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가
연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를
갖는 경우를 triplet이라고 한다.
6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
6자리 숫자를 입력받아 baby-gin 여부를 판단하는 프로그램 작성하라.
'''
'''
입력 예)
667767 # 1
054060 # 1
101123 # 0
'''


T = int(input())
for tc in range(T):
    numli = list(map(int,input()))
    a = [0] * 12
    triplet = 0
    run1 = 0
    for i in numli:
        a[i] += 1
    i=0
    while i <= 9:
        if a[i] >= 3:
            a[i] -= 3
            triplet += 1
            continue
        elif a[i] >= 1 and a[i+1] >= 1 and a[i+2] >= 1:
            a[i] -=1
            a[i+1] -=1
            a[i+2] -=1
            run1 += 1
            continue
        i+=1
    if triplet + run1 == 2:
        print(f"#{tc+1} 1")
    else:
        print(f"#{tc+1} 0")
