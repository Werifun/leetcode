'''
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    """
    思路：
    1、保证每一列的第一个数字为1(翻转行)，因为后几位累加也不可能有最高位的数值大
    2、以后每列选取 1 最多的情况(按列翻转即可)
    """
    def matrixScore(self, A: List[List[int]]) -> int:
        ans = 0
        if len(A) <= 0: return ans

        for row_id, row in enumerate(A):
            if row[0] == 0:
                A[row_id] = self.reverse_1(row)

        num_row = len(A)  # 行数
        for col_id in range(len(A[0])):
            zhishu = 0
            for row_id in range(len(A)):
                zhishu += A[row_id][col_id]
            ans = ans*2 + max(zhishu, num_row-zhishu)  # ans*2是进位，max是取当前为1最多的情况
            # print(ans,zhishu,num_row -zhishu)
        # print(A)
        return ans


    @classmethod
    def reverse_1(self, row):
        # new_row = [0]*len(row)
        for num_id, num in enumerate(row):
            row[num_id] = 1-num

        return row 


        