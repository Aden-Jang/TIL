class Solution:
    def isPalindrome(self, s: str) -> bool:
        strin = []
        # 
        for i in s:
            if i.isalnum():
                strin.append(i.lower())
        rstrin = list(reversed(strin))
        return strin == rstrin

'''
# 시험 시행
s = input()
strin = []
# 숫자나 문자만 소문자형태로 strin리스트에 저장
for i in s:
    if i.isalnum():
        strin.append(i.lower())
# rstrin에 strin의 리버스값을 저장
rstrin = list(reversed(strin))
# True/False값으로 프린트
print(strin == rstrin)
'''