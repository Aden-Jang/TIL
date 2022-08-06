class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        a = []
        b = []
        for i in logs:
            # 숫자와 문자를 리스트로 나눔
            if i[-1].isdigit():
                a.append(i)
            else:
                b.append(i)
        b.sort()
        # b의 첫번째 단어부터 정렬, 같으면 0번째 단어순으로 정렬
        b = sorted(b, key=lambda x: (x.split()[1:], x.split()[0]))
        return b + a
'''
# 시험 시행
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
a = []
b = []
for i in logs:
    # 숫자와 문자를 리스트로 나눔
    if i[-1].isdigit():
        a.append(i)
    else:
        b.append(i)
print(a)
b.sort()
# b의 첫번째 단어부터 정렬, 같으면 0번째 단어순으로 정렬
b = sorted(b, key=lambda x: (x.split()[1:], x.split()[0]))
print(b + a)
'''