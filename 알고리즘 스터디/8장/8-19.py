class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next