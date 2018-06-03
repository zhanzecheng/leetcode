# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/2 上午11:49
# @Author  : zhanzecheng
# @File    : 22.产生合法括号.py
# @Software: PyCharm
"""

import copy
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generate(n, 0, "")
        return self.result
    def generate(self, m, n, tmp):
        if m == 0 and n == 0:
            self.result.append(tmp)
            return

        if n > 0:
            t = copy.copy(tmp)
            t += ')'
            self.generate(m , n - 1, t)
        if m > 0:
            t = copy.copy(tmp)
            t += '('
            self.generate(m - 1, n + 1, t)
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))