# 풀이 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

# 풀이 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()