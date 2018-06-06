# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 上午10:45
# @Author  : zhanzecheng
# @File    : 131.回文字符串划分.py
# @Software: PyCharm
"""


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, t):
        if len(s) == 0:
            self.result.append(t.copy())
            return
        for i in range(0, len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                t.append(s[:i+1])
                self.dfs(s[i+1:], t)
                # dfs的pop
                t.pop()

if __name__ == '__main__':
    solution = Solution()
    data = 'aab'
    print(solution.partition(data))