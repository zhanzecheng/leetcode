# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 上午10:45
# @Author  : zhanzecheng
# @File    : 131.回文字符串划分.py
# @Software: PyCharm
"""

# 这道题使用dfs来暴力搜索解决

# TODO: check 1

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        re = []

        def dfs(string, path):
            if len(string) == 0:
                re.append(path)
                return

            for i in range(len(string)):
                # 注意这里的i+1
                if string[:i + 1] == string[:i + 1][::-1]:
                    dfs(string[i + 1:], path + [string[:i + 1]])

        dfs(s, [])
        return re

if __name__ == '__main__':
    solution = Solution()
    data = 'aab'
    print(solution.partition(data))