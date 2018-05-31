# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 上午9:16
# @Author  : zhanzecheng
# @File    : 93.存储IP地址.py
# @Software: PyCharm
"""

# 又是一道DFS的题目

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.dfs(s, 0, '')
        return self.result
    def dfs(self, s, index, res):

        if index == 4:
            if len(s) == 0:
                self.result.append(res[:-1])
            return

        for i in range(1, 4):
            if i <= len(s):
                if i == 2:
                    if s[0] != '0':
                        self.dfs(s[i:], index+1, res + str(s[:i]) + '.')
                elif i == 1:
                    self.dfs(s[i:], index + 1, res + str(s[:i]) + '.')
                else:
                    if int(s[:i]) <= 255 and s[0] != '0':
                        self.dfs(s[i:], index + 1, res + str(s[:i]) + '.')

if __name__ == '__main__':
    solution = Solution()
    data = "25525511135"
    print(solution.restoreIpAddresses(data))