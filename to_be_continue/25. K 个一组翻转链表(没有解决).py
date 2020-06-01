# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre_head = ListNode(0)
        pre_head.next = head
        pre = pre_head
        while head:
            tail = pre

            for i in range(k):
                tail = tail.next
                if not tail:
                    return pre_head.next
                next_node = tail.next
            # print(head, tail)
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = next_node
            pre = tail
            head = tail.next

        return pre_head.next

########### 我的reverse  有环， 不知道为什么
    # def reverse(self, head, tail):
    #     if not head or head==tail:
    #         return head, tail
    #     pre = None
    #     cur = head
    #     later = head.next
    #     while cur and later:
    #         cur.next = pre
    #         pre = cur
    #         cur = later
    #         later = later.next
    #     cur.next = pre
    #     print(cur, head)
    #     return cur, head

    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head