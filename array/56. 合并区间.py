'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
1先对区间按照左端点升序排序，然后遍历。
2：如果当前遍区间的左端点 <= 结果集中最后一个区间的右端点，说明它们有交集，此时把区间添加到结果集；
3否则没有交集

作者：feng-hua-zheng-mao-7
链接：https://leetcode-cn.com/problems/merge-intervals/solution/li-yong-zhan-jin-xing-bian-li-by-feng-hua-zheng-ma/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        intervals = sorted(intervals,key=lambda x: x[0])  # 注意sorted的使用
        # intervals.sort(key=lambda x:x[0])
        cur_it = None
        ret = []
        for interval in intervals:
            if not cur_it:  # 初始化
                cur_it = interval
                continue
            if cur_it[1] >= interval[0]:
                cur_it[1]=max(interval[1], cur_it[1])
            else:
                ret.append(cur_it)
                cur_it = interval
        if cur_it:  # skip if cur_it == None
            ret.append(cur_it)
        return ret
