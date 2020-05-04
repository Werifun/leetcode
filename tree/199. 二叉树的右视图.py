"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    思路：很简单
    前序遍历：根左右，用height记录每个节点所在高度，遍历的过程中同一高度的最右侧的节点必然在最后一次出现，直接用right_list维护当前已遍历路径最右侧的节点
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_list=[]
        if not root: return right_list

        self.pre_order(root, 0, right_list)

        return right_list

    def pre_order(self, node, height,right_list):
        if not node:
            return
        if len(right_list)>height:
            right_list[height] = node.val
        elif len(right_list)==height:
            right_list.append(node.val)
            # print(right_list)
        else:
            raise Error('right_list have false!')

        self.pre_order(node.left, height+1, right_list)
        self.pre_order(node.right, height+1, right_list)

        return