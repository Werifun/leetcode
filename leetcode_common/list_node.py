# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_list2listnode(l):
    node_l = []
    for x in l:
        node_l.append(ListNode(x))

    pre_node = None
    for node in node_l:
        if not pre_node:
            pre_node = node
        else:
            pre_node.next = node
            pre_node = node
    return node_l[0]


def print_node(node):
    a = node
    while(a):
        print(a.val)
        a = a.next

    return


if __name__ == '__main__':
    b = convert_list2listnode([1,2,3,4,5])
    print_node(b)
