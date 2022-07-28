T = int(input())
for i in range(T):
    a, b = input().split()
    a = list(map(int, a))
    b = int(b)
    for j in range(b):
        if max(a) 

'''
def cal(chan, cnt, k, nums_c):
 
    if chan == cnt:
        str_num = list( map(str,nums_c) )
        int_num = int("".join(str_num))
        global maxx
        if maxx< int_num:
            maxx = int_num
        # print(int_num)
        return
    else:
        piv = nums_c[k]
        temp = nums_c[k+1:]
        val = max(temp)
        if val > piv:                     ## 바꿀 수 있을 때
            for i in range(len(temp)):
                if temp[i] == val:
                    cop = nums_c[:]
                    cop[k], cop[i+k+1] = cop[i+k+1], cop[k]
                    cal(chan,cnt+1,k+1,cop)
        else:  # 바꿀 수 없을 때,
            if k == len(nums_c)-2:
                if len(set(nums_c)) < len(nums_c):  ## 중복 있을 때 그대로
                    cal(chan, chan, k + 1, nums_c)
                    return
                else:
                    if (chan-cnt)%2 == 0:
                        cal(chan, chan, k + 1, nums_c)
                        return
                    else:
                        nums_c[-1], nums_c[-2] = nums_c[-2], nums_c[-1]
                        cal(chan, chan, k + 1, nums_c)
                        return
            else:
                cal(chan, cnt, k+1, nums_c)
 
 
 
 
T = int(input())
for _ in range(10):
 
    nums, chan = map(int,input().split())
    nums = list(map(int,str(nums)))
    # print(nums)
    cnt = 0
    maxx = -1
    cal(chan, cnt, 0, nums)
    print("#{} {}".format(_+1, maxx))
'''