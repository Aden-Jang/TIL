def solve():
    for idx in range(len(lst2)):    # idx: 0<->1 변경할 위치
        # [1] 가능한 비트하나 정정해서 10진수로 변환
        lst2[idx] = (lst2[idx]+1)%2
        num = 0
        for n in lst2:
            num = n + num*2

        # [2] 3진수로 변환
        conv3 = []
        t = num
        while t>0:
            conv3.insert(0, t%3)
            t//=3

        # [3] 각 위치별로 다른 개수 카운트
        cnt = 0
        tlst1 = conv3[::-1]
        tlst2 = lst3[::-1]
        for i in range(min(len(tlst1), len(tlst2))):
            if tlst1[i]!=tlst2[i]:
                cnt+=1
        cnt+= abs(len(tlst1)-len(tlst2))
        #
        #
        # for i in range(-1, -(min(len(conv3), len(lst3))-1), -1):
        #    if conv3[i]!=lst3[i]:
        #       cnt+=1
        # # 자리수가 다르다면 그 길이차이만큼 다른 개수임
        # cnt += abs(len(conv3)-len(lst3))

        if cnt==1:
            return num

        lst2[idx] = (lst2[idx]+1)%2 # 원래대로


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve()
    print(f'#{test_case} {ans}')