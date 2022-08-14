for i in range(1,11):
    e=0
    a = int(input())
    b = list(map(int,input().split()))
    for j in range(2,a-2):
        c = [b[j-2],b[j-1],b[j],b[j+1],b[j+2]] # 양옆 2칸까지의 값을 리스트로 생성
        if max(c) == c[2]: # 중앙이 가장 크면 뽑아내고 2번째로 큰 값에서 뺌, 답에 더해줌
            d = c.pop(2)
            e += d - max(c)
    print(f'#{i} {e}')