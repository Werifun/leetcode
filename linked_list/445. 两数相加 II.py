'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        l3 = ListNode(0)
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        s = []
        carry = 0
        while s1 or s2:
            num1 = s1.pop() if s1 else 0
            num2 = s2.pop() if s2 else 0
            s.append((num1+num2+carry)%10)
            carry = (num1+num2+carry)//10

        if carry:
            l3.next = ListNode(1)
            l3_step = l3.next
        else:
            l3_step = l3
        while s:
            cur_node = ListNode(s.pop())
            l3_step.next = cur_node
            l3_step = cur_node
        return l3.next

