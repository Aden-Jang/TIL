# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q=[]
        # 연결 리스트를 리스트로 변환 
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        # 리스트의 절반까지만 반대편 위치와 같은지 확인, 다르면 False 리턴
        for i in range(len(q)//2):
            if q[i] != q[-i-1]:
                return False
        # 끝까지 잘 돌면 True 리턴
        return True