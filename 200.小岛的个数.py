# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/7 下午4:49
# @Author  : zhanzecheng
# @File    : 200.小岛的个数.py
# @Software: PyCharm
"""

# TODO: check 1 turn 1 to 0 and count

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        def dfs(i, j):
            row = len(grid)
            col = len(grid[0])
            if i >= row:
                return
            if j >= col:
                return
            if i < 0:
                return
            if j < 0:
                return
            if grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
if __name__ == '__main__':
    solution = Solution()
    data = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
