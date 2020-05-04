'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点?(i,?ai) 。在坐标内画 n 条垂直线，垂直线 i?的两个端点分别为?(i,?ai) 和 (i, 0)。找出其中的两条线，使得它们与?x?轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且?n?的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        贪婪思想：
        1、让水底的长度最大，然后逐步缩小底部的长度，但是保持高度最大
        """
        max_water = 0
        if len(height)<2:
            return max_water
        
        left_index, right_index = 0, len(height)-1
        # max_water = max(max_water, max(height[0], height[-1])*(end-start))

        while left_index < right_index:
            left_height, right_height = height[left_index], height[right_index]
            max_water = max(max_water, min(left_height, right_height)*(right_index-left_index))

            if left_height < right_height:
                left_index += 1
            else: right_index -= 1

        return max_water
        
