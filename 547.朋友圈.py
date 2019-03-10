# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/17 上午11:09
# @Author  : zhanzecheng
# @File    : 547.朋友圈.py
# @Software: PyCharm
"""

# 考察的核心点还是 连通图 dfs visit标识矩阵
# 这一题的难度是简单的

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        length = len(M)
        visit = [0] * length

        count = 0

        def dfs(cur):

            for j in range(length):
                if visit[j] == 0 and M[cur][j] == 1:
                    visit[j] = 1
                    dfs(j)

        for i in range(length):
            if visit[i] != 1:
                visit[i] = 1

                dfs(i)

                count += 1
        return count