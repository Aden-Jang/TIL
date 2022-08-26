# sw = int(input())
# swlst = list(map(int, input().split()))
# st = int(input())
# stlst = [list(map(int, input().split())) for _ in range(st)]
#
#
# for i in range(st):
#     a = stlst[i][1]
#     if stlst[i][0] == 1:
#         while a <= sw:
#             swlst[a-1] = (swlst[a-1] + 1) % 2
#             a += stlst[i][1]
#     else:
#         swlst[a-1] = (swlst[a-1] + 1) % 2
#         k = 1
#         while 0 <= a-k-1 and a+k-1 <= sw:
#             if swlst[a-k-1] == swlst[a+k-1]:
#                 swlst[a-k-1] = (swlst[a-k-1] + 1) % 2
#                 swlst[a+k-1] = (swlst[a+k-1] + 1) % 2
#                 k += 1
#             else:
#                 break
# print(*swlst)



sw = int(input())
swlst = list(map(int, input().split()))
st = int(input())
for _ in range(st):
    sts, stn = map(int, input().split())

    a = stn
    if sts == 1:
        while a <= sw:
            if swlst[a-1] == 0:
                swlst[a - 1] = 1
            else:
                swlst[a - 1] = 0
            a += stn
    else:
        if swlst[a - 1] == 0:
            swlst[a - 1] = 1
        else:
            swlst[a - 1] = 0
        k = 1
        while 0 <= a-k-1 and a+k-1 < sw:
            if swlst[a-k-1] == swlst[a+k-1]:
                if swlst[a - k - 1] == 0:
                    swlst[a - k - 1] = 1
                else:
                    swlst[a - k - 1] = 0
                if swlst[a + k - 1] == 0:
                    swlst[a + k - 1] = 1
                else:
                    swlst[a + k - 1] = 0
                k += 1
            else:
                break
aa = 0
for i in range(sw):
    if aa == 20:
        aa -= 20
        print()
    print(swlst[i], end=' ')
    aa += 1
