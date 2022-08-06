class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for idx, a in enumerate(strs):
            # 각 단어를 알파벳 순서로 정렬
            a = ''.join(sorted(a))
            l.append([idx,a])

        # l리스트의 a값으로 정렬
        l=sorted(l, key = lambda x : x[1])
        print(l)
        ans = dict()

        # 딕셔너리에 기존 값 + 해당 값 (해당 키가 없으면 빈리스트에 해당값 추가)
        for i in range(len(l)):
            ans[l[i][1]] = ans.get(l[i][1],[]) + [strs[l[i][0]]]

        return list(ans.values())

'''
# 시험 시행
strs = ['eat','tea','tan','ate','nat','bat']
l = []
for idx, a in enumerate(strs):
    # 각 단어를 알파벳 순서로 정렬
    a = ''.join(sorted(a))
    l.append([idx,a])

# l리스트의 a값으로 정렬
l=sorted(l, key = lambda x : l[1])
print(l)
ans = dict()
# 딕셔너리에 기존 값 + 해당 값 (해당 키가 없으면 빈리스트에 해당값 추가)
for i in range(len(l)):
    ans[l[i][1]] = ans.get(l[i][1],[]) + [strs[l[i][0]]]

print(list(ans.values()))

# 타임오버
strs = ['eat','tea','tan','ate','nat','bat']
a = []
for i in strs:
    if sorted(i) not in a:
        a.append(sorted(i))
b = [[] for _ in range(len(a))]
for i in range(len(strs)):
    for j in range(len(a)):
        if sorted(strs[i]) == a[j]:
            b[j].append(strs[i])
print(b)

'''