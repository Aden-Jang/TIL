class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a=[]
        for i in paragraph:
            a.append(i)
        for i in range(len(a)):
            if a[i].isalnum() == False:
                a[i] = ' '
        a = ''.join(a)
        a = a.lower()
        b = list(a.split())
        print(b)

        c = [0]*len(b)
        bb = list(set(b))
        for i in banned:
            if i in bb:
                bb.remove(i)
        print(bb)
        for i in range(len(b)):
            if b[i] not in bb:
                continue
            else:
                c[bb.index(b[i])] += 1
        return bb[c.index(max(c))]

'''
# 시험 시행
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

a=[]
for i in paragraph:
    a.append(i)
# 리스트를 쭉 돌리면서 문자나 숫자 아니면 공백으로 대체
for i in range(len(a)):
    if a[i].isalnum() == False:
        a[i] = ' '
a = ''.join(a)
a = a.lower()
b = list(a.split())

bb = list(set(b))
# bb안에 밴될 단어가 있다면 삭제
for i in banned:
    if i in bb: # 이거 안쓰면 ban할 값이 bb에 없으면 remove가 안되서 에러남
        bb.remove(i)
c = [0]*len(bb)
# bb에 없는 단어들(ban한 단어들)은 패스
for i in range(len(b)):
    if b[i] not in bb:
        continue
    # ban안한 값이 있는 경우 bb의 해당 단어에 해당하는 인덱스에 1을 더해줌
    else:
        c[bb.index(b[i])] += 1
# bb의 가장 많은 값의 인덱스를 프린트  
print(bb[c.index(max(c))])
'''




# 틀림

# paragraph = paragraph.lower()
# paragraph = list(paragraph.split())
# a = list(set(paragraph))
# b=[]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j].isalnum() == False:
#             b.append(a[i].replace(a[i][j],'')) # b,b,b,c, d에서 bbbc로 됨
#             break
#         elif j == len(a[i])-1:
#             b.append(a[i])
#             break
#         else:
#             continue

# c = [0]*len(b)
# bb = list(set(b))
# for i in banned:
#     if i in bb:
#         bb.remove(i)
# print(bb)
# for i in range(len(b)):
#     if b[i] not in bb:
#         continue
#     else:
#         c[bb.index(b[i])] += 1
# print(bb[c.index(max(c))])







