'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """使用广度搜索"""
        res = 0
        rows = len(grid)
        if rows==0:return res
        cols = len(grid[0])
        if cols==0:return res
        bools = [[0]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if bools[row][col] == 1: continue
                if grid[row][col]=='1' :
                    res+=1
                    self.dfs(grid, bools, rows, cols, row, col)

        return res

    def dfs(self, grid, bools, rows, cols, row, col):
        if row>=rows: return
        if col>=cols: return
        if row<0: return
        if col<0: return
        if bools[row][col] == 1: return
        if grid[row][col] == '0':
            bools[row][col] = 1
            return
        else:
            bools[row][col] = 1
            self.dfs(grid, bools, rows, cols, row+1, col)
            self.dfs(grid, bools, rows, cols, row-1, col)
            self.dfs(grid, bools, rows, cols, row, col+1)
            self.dfs(grid, bools, rows, cols, row, col-1)

        return