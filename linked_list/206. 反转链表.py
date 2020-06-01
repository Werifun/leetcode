# coding: utf-8
from leetcode_common.list_node import convert_list2listnode,ListNode, print_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    经典的题，终于直接做出来了，但是还是花了十几分钟，不开心
    递归的方法目前没有思路
    """
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 长度是0，或者是1的时候，直接返回
            return head
        # 用三个点，记录位置，逐步探索出来的
        pre = None
        cur = head
        later = head.next

        while cur and later:
            cur.next = pre
            pre = cur
            cur = later
            later = later.next

        cur.next = pre

        return cur
    """
    def __init__(self):
        self.new_head = None
    # 搞个递归版本
    # 自己写的递归版本为什么不行呢，里面有环了
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 长度是0，或者是1的时候，直接返回
            return head
        new_head = None
        self.recursive(head, new_head)

        return self.new_head

    def recursive(self, head, new_head):
        if not head.next:
            new_head = head
            self.new_head = head
            # print(self.new_head.val)
            # print(new_head.val)
            return new_head
        a = self.recursive(head.next, new_head)
        a.next = head
        head.next = None  # 破解 链表中的 环
        # print('其他情况下的newhead', new_head)
        return head

if __name__ == '__main__':
    inp = convert_list2listnode([1,2,3,4,566])
    s = Solution()
    b = s.reverseList(inp)
    print_node(b)