'''
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        思路：
        举例 [2,2,2,1,2,2,1] k=1
        1的index是3和6。
        第一个1(满足k=1的条件)左边有四种可能(0-3个2, 3-(-1), -1相当于第0个奇数的索引,事实上不存在，3是第一个奇数1的索引)，右边有3中可能(0-2个2)因此，res=(3-(-1))*(6-3)=12
        第二个1(满足k=1的条件)左边有三种可能(0-2个2)，右边有1中可能(0个2)因此，res=(6-3*(7-6)=3
        所以总共有12+3=15中可能
        """
        if k <= 0: return 0
        res = 0  # 返回结果
        q = []  # 记录当前的子数组最大长度
        odd_index = [-1]  # 记录所有奇数的索引，默认第0个奇数的索引为-1(事实上不存在第0个奇数，为了方便计算)
        count_odd = 0  # 记录当前奇数的个数，与k比较
        for num_id, num in enumerate(nums):
            if num %2 : 
                if count_odd == k:
                    res += self.calc_sub_list(q, odd_index, num_id)
                    count_odd -= 1
                q.append(num)
                odd_index.append(num_id)
                count_odd += 1
            else:
                q.append(num)
        else:  # for循环结束，如果满足[优美子数组]条件，计算
            if count_odd == k:
                res += self.calc_sub_list(q, odd_index, len(nums))
                    
        return res

    def calc_sub_list(self, q, odd_index, num_id):
        """
        1、计算优美子数组的个数
        2、并更新 odd_index和q
        3、变量名起的不好
        """
        assert len(odd_index) >= 2
        # print(odd_index, num_id)
        res = (odd_index[1]-odd_index[0])*(num_id-odd_index[-1])
        odd_index.pop(0)
        # print(res,odd_index, num_id)
        while len(q)>0 and q[0]%2==0:
            q.pop(0)
        q.pop(0)
        # print(q)

        return res
